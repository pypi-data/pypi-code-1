# -*- coding: cp1252 -*-
options = None
if __name__ == "__main__":

    PSYCO = 0

    import xlrd
    import sys, time, glob, traceback, pprint, gc

    null_cell = xlrd.empty_cell

    def show_row(bk, sh, rowx, colrange, printit):
        if printit: print
        if bk.formatting_info:
            for colx, ty, val, cxfx in get_row_data(bk, sh, rowx, colrange):
                if printit:
                    print "cell %s%d: type=%d, data: %r, xfx: %s" \
                        % (xlrd.colname(colx), rowx+1, ty, val, cxfx)
        else:
            for colx, ty, val, _unused in get_row_data(bk, sh, rowx, colrange):
                if printit:
                    print "cell %s%d: type=%d, data: %r" % (xlrd.colname(colx), rowx+1, ty, val)

    def get_row_data(bk, sh, rowx, colrange):
        result = []
        dmode = bk.datemode
        ctys = sh.row_types(rowx)
        cvals = sh.row_values(rowx)
        for colx in colrange:
            cty = ctys[colx]
            cval = cvals[colx]
            if bk.formatting_info:
                cxfx = str(sh.cell_xf_index(rowx, colx))
            else:
                cxfx = ''
            if cty == xlrd.XL_CELL_DATE:
                try:
                    showval = xlrd.xldate_as_tuple(cval, dmode)
                except xlrd.XLDateError:
                    e1, e2 = sys.exc_info()[:2]
                    showval = "%s:%s" % (e1.__name__, e2)
                    cty = xlrd.XL_CELL_ERROR
            elif cty == xlrd.XL_CELL_ERROR:
                showval = xlrd.error_text_from_code.get(cval, '<Unknown error code 0x%02x>' % cval)
            else:
                showval = cval
            result.append((colx, cty, showval, cxfx))
        return result

    def bk_header(bk):
        print
        print "BIFF version: %s; datemode: %s" \
            % (xlrd.biff_text_from_num[bk.biff_version], bk.datemode)
        print "codepage: %r (encoding: %s); countries: %r" \
            % (bk.codepage, bk.encoding, bk.countries)
        print "last saved by: %r" % bk.user_name
        print "nsheets: %d; sheet names: %r" % (bk.nsheets, bk.sheet_names())
        print "Pickleable: %d; Use mmap: %d; Formatting: %d" \
            % (bk.pickleable, bk.use_mmap, bk.formatting_info)
        print "FORMATs: %d, FONTs: %d, XFs: %d" \
            % (len(bk.format_list), len(bk.font_list), len(bk.raw_xf_list))
        print "Load time: %.2f seconds (stage 1) %.2f seconds (stage 2)" \
            % (bk.load_time_stage_1, bk.load_time_stage_2)
        print

    def show_names(bk, dump=0):
        bk_header(bk)
        if bk.biff_version < 50:
            print "Names not extracted in this BIFF version"
            return
        nlist = bk.name_obj_list
        print "Name list: %d entries" % len(nlist)
        for nobj in nlist:
            if dump:
                nobj.dump(sys.stdout,
                    header="\n=== Dump of name_obj_list[%d] ===" % nobj.name_index)
            else:
                print "[%d]\tName:%r macro:%r scope:%d\n\tresult:%r\n" \
                    % (nobj.name_index, nobj.name, nobj.macro, nobj.scope, nobj.result)

    def print_labels(sh, labs, title):
        if not labs:return
        for rlo, rhi, clo, chi in labs:
            print "%s label range %s:%s contains:" \
                % (title, xlrd.cellname(rlo, clo), xlrd.cellname(rhi-1, chi-1))
            for rx in xrange(rlo, rhi):
                for cx in xrange(clo, chi):
                    print "    %s: %r" % (xlrd.cellname(rx, cx), sh.cell_value(rx, cx))

    def show_labels(bk):
        # bk_header(bk)
        hdr = 0
        for shx in range(bk.nsheets):
            sh = bk.sheet_by_index(shx)
            clabs = sh.col_label_ranges
            rlabs = sh.row_label_ranges
            if clabs or rlabs:
                if not hdr:
                    bk_header(bk)
                    hdr = 1
                print "sheet %d: name = %r; nrows = %d; ncols = %d" % \
                    (shx, sh.name, sh.nrows, sh.ncols)
                print_labels(sh, clabs, 'Col')
                print_labels(sh, rlabs, 'Row')

    def show(bk, nshow=65535, printit=1):
        bk_header(bk)
        if 0:
            rclist = xlrd.sheet.rc_stats.items()
            rclist.sort()
            print "rc stats"
            for k, v in rclist:
                print "0x%04x %7d" % (k, v)
        if options.onesheet:
            try:
                shx = int(options.onesheet)
            except ValueError:
                shx = bk.sheet_by_name(options.onesheet).number
            shxrange = [shx]
        else:
            shxrange = range(bk.nsheets)
        # print "shxrange", shxrange
        for shx in shxrange:
            sh = bk.sheet_by_index(shx)
            nrows, ncols = sh.nrows, sh.ncols
            colrange = range(ncols)
            anshow = min(nshow, nrows)
            print "sheet %d: name = %r; nrows = %d; ncols = %d" % \
                (shx, sh.name, sh.nrows, sh.ncols)
            if nrows and ncols:
                # Attempt to access the RHS corners
                sh.row_types(0)[ncols-1]
                sh.row_values(0)[ncols-1]
                sh.row_types(nrows-1)[ncols-1]
                sh.row_values(nrows-1)[ncols-1]
            for rowx in xrange(anshow-1):
                if not printit and rowx % 10000 == 1 and rowx > 1:
                    print "done %d rows" % (rowx-1,)
                show_row(bk, sh, rowx, colrange, printit)
            if anshow and nrows:
                show_row(bk, sh, nrows-1, colrange, printit)
            print

    def count_xfs(bk):
        bk_header(bk)
        for shx in range(bk.nsheets):
            sh = bk.sheet_by_index(shx)
            nrows, ncols = sh.nrows, sh.ncols
            print "sheet %d: name = %r; nrows = %d; ncols = %d" % \
                (shx, sh.name, sh.nrows, sh.ncols)
            if nrows and ncols:
                # Attempt to access the RHS corners
                sh.row_types(0)[ncols-1]
                sh.row_values(0)[ncols-1]
                sh.row_types(nrows-1)[ncols-1]
                sh.row_values(nrows-1)[ncols-1]
            # Access all xfindexes to force gathering stats
            type_stats = [0, 0, 0, 0, 0, 0, 0]
            for colx in xrange(ncols):
                for rowx in xrange(nrows):
                    xfx = sh.cell_xf_index(rowx, colx)
                    assert xfx >= 0
                    cty = sh.cell_type(rowx, colx)
                    type_stats[cty] += 1
            print "XF stats", sh._xf_index_stats
            print "type stats", type_stats
            print

    def main(cmd_args):
        import optparse
        global options
        usage = "%prog [options] command [input-file-patterns]"
        oparser = optparse.OptionParser(usage)
        oparser.add_option(
            "-l", "--logfilename",
            default="",
            help="contains error messages")
        oparser.add_option(
            "-v", "--verbosity",
            type="int", default=0,
            help="level of information and diagnostics provided")
        oparser.add_option(
            "-p", "--pickleable",
            type="int", default=1,
            help="1: ensure Book object is pickleable (default); 0: don't bother")
        oparser.add_option(
            "-m", "--mmap",
            type="int", default=-1,
            help="1: use mmap; 0: don't use mmap; -1: accept heuristic")
        oparser.add_option(
            "-e", "--encoding",
            default="",
            help="encoding override")
        oparser.add_option(
            "-f", "--formatting",
            type="int", default=0,
            help="0 (default): no fmt info\n"
                 "1: fmt info (all cells)\n"
                 "2: fmt info (margins trimmed)\n"
            )
        oparser.add_option(
            "-g", "--gc",
            type="int", default=0,
            help="0: auto gc enabled; 1: auto gc disabled, manual collect after each file; 2: no gc")
        oparser.add_option(
            "-s", "--onesheet",
            default="",
            help="restrict output to this sheet (name or index)")

        options, args = oparser.parse_args(cmd_args)
        if len(args) == 1 and args[0] in ("version", ):
            pass
        elif len(args) < 2:
            oparser.error("Expected al least 2 args, found %d" % len(args))
        cmd = args[0]
        xlrd_version = getattr(xlrd, "__VERSION__", "unknown; before 0.5")
        if cmd == 'dump':
            xlrd.dump(args[1])
            sys.exit(0)
        if cmd == 'count_records':
            xlrd.count_records(args[1])
            sys.exit(0)
        if cmd == 'version':
            print "xlrd: %s, from %s" % (xlrd_version, xlrd.__file__)
            print "Python:", sys.version
            sys.exit(0)
        if options.logfilename:
            logfile = open(options.logfilename, 'w')
        else:
            logfile = sys.stdout
        mmap_opt = options.mmap
        mmap_arg = xlrd.USE_MMAP
        if mmap_opt in (1, 0):
            mmap_arg = mmap_opt
        elif mmap_opt != -1:
            print 'Unexpected value (%r) for mmap option -- assuming default' % mmap_opt
        fmt_opt = options.formatting
        gc_mode = options.gc
        if gc_mode:
            gc.disable()
        for pattern in args[1:]:
            for fname in glob.glob(pattern):
                print >> logfile, "\n=== File: %s ===" % fname
                if gc_mode == 1:
                    n_unreachable = gc.collect()
                    if n_unreachable:
                        print >> logfile, "GC before open:", n_unreachable, "unreachable objects"
                try:
                    t0 = time.time()
                    bk = xlrd.open_workbook(fname,
                        verbosity=options.verbosity, logfile=logfile,
                        pickleable=options.pickleable, use_mmap=mmap_arg,
                        encoding_override=options.encoding,
                        formatting_info=fmt_opt,
                        )
                    t1 = time.time()
                    print >> logfile, "Open took %.2f seconds" % (t1-t0,)
                except xlrd.XLRDError:
                    print >> logfile, "*** Open failed: %s: %s" % sys.exc_info()[:2]
                    continue
                except KeyboardInterrupt:
                    print >> logfile, "*** KeyboardInterrupt ***"
                    traceback.print_exc(file=logfile)
                    sys.exit(1)
                except:
                    print >> logfile, "*** Open failed ***"
                    traceback.print_exc(file=logfile)
                    continue
                t0 = time.time()
                if cmd == 'hdr':
                    bk_header(bk)
                elif cmd == 'ov': # OverView
                    show(bk, 0)
                elif cmd == 'show': # all rows
                    show(bk)
                elif cmd == '2rows': # first row and last row
                    show(bk, 2)
                elif cmd == '3rows': # first row, 2nd row and last row
                    show(bk, 3)
                elif cmd == 'bench':
                    show(bk, printit=False)
                elif cmd == 'names': # named reference list
                    show_names(bk)
                elif cmd == 'name_dump': # named reference list
                    show_names(bk, dump=1)
                elif cmd == 'labels':
                    show_labels(bk)
                elif cmd == 'xfc':
                    count_xfs(bk)
                else:
                    print >> logfile, "*** Unknown command <%s>" % cmd
                    sys.exit(1)
                del bk
                if gc_mode == 1:
                    n_unreachable = gc.collect()
                    if n_unreachable:
                        print >> logfile, "GC post cmd:", fname, "->", n_unreachable, "unreachable objects"
                t1 = time.time()
                print >> logfile, "\ncommand took %.2f seconds\n" % (t1-t0,)

        return None

    av = sys.argv[1:]
    if not av:
        main(av)
    firstarg = av[0].lower()
    if firstarg == "hotshot":
        import hotshot, hotshot.stats
        av = av[1:]
        prof_log_name = "XXXX.prof"
        prof = hotshot.Profile(prof_log_name)
        # benchtime, result = prof.runcall(main, *av)
        result = prof.runcall(main, *(av, ))
        print "result", repr(result)
        prof.close()
        stats = hotshot.stats.load(prof_log_name)
        stats.strip_dirs()
        stats.sort_stats('time', 'calls')
        stats.print_stats(20)
    elif firstarg == "profile":
        import cProfile
        av = av[1:]
        cProfile.run('main(av)', 'YYYY.prof')
        import pstats
        p = pstats.Stats('YYYY.prof')
        p.strip_dirs().sort_stats('cumulative').print_stats(30)

    else:
        main(av)
