#!/usr/bin/python
# -*- coding: utf-8 -*-

from qt import *
from Epigrass.manager import *
from threading import *
from Epigrass.cpanel import MainPanel
from Epigrass.about import aboutDialog
import os,sys,ConfigParser, string, pwd, copy, commands
import Epigrass.epiplay as epi
from Epigrass import spread


class MainPanel_Impl(MainPanel):

    def __init__(self,parent = None,name = None,fl = 0):
        
        # set Translation
        self.curdir = os.getcwd()
        os.chdir(pwd.getpwuid(os.getuid())[5])
        if os.access('.epigrassrc',os.F_OK):
            try:
                self.conf = self.loadRcFile('.epigrassrc')
                lang = self.conf['settings.language']
            except: 
                lang = ''
            #print lang
        else: lang = ''
        tr = QTranslator(app)
        loadLang(app,tr,lang)
        
        MainPanel.__init__(self,parent,name,fl)
        # Overload connections
        self.connect(self.editButton,SIGNAL("released()"),self.editScript)
        self.connect(self.chooseButton,SIGNAL("released()"),self.chooseScript)
        self.connect(self.buttonExit,SIGNAL("released()"),self.onExit)
        self.connect(self.buttonRun,SIGNAL("released()"),self.onRun)
        self.connect(self.buttonHelp,SIGNAL("released()"),self.onHelp)
        self.connect(self.dbBackup,SIGNAL("released()"),self.onDbBackup)
        self.connect(self.dbInfo,SIGNAL("released()"),self.onDbInfo)
        self.connect(self.repOpen,SIGNAL("released()"),self.onRepOpen)
        self.connect(self.playButton,SIGNAL("released()"),self.onPlayButton)
        self.connect(self.dbscanButton,SIGNAL("released()"),self.onVisual)
        self.connect(self.consensusButton,SIGNAL("released()"),self.onConsensus)
        self.connect(self.tableList,SIGNAL("activated(int)"),self.getVariables)
        self.connect(self.dbType,SIGNAL("activated(int)"),self.setBackend)
        #check if rc file exists if not, creates one

        usern = pwd.getpwuid(os.getuid())[0] #Get the user name
        os.chdir(pwd.getpwuid(os.getuid())[5])
        if not os.access('.epigrassrc',os.F_OK):
            self.initRc()

        else:#read existing configuration file
            self.conf = self.loadRcFile('.epigrassrc')
            self.fillGui(self.conf)
        self.sim = None
            
    def initRc(self):
        """
        Initializes the epigrassrc file.
        """
        usern = pwd.getpwuid(os.getuid())[0] #Get the user name
        os.chdir(pwd.getpwuid(os.getuid())[5])
        os.mknod('.epigrassrc')
        f = open('.epigrassrc','w')
        
        rcskel = ['#EpiGrass Configuration File',
            '[model]',
            'script=script.epg',
            '[database]',
            'backend=sqlite',
            'host=localhost',
            'port=3306',
            'user=epigrass',
            '[settings]',
            'name=John Doe',
            'editor=kate',
            'pdfviewer=kghostview',
            'language=en'
            ]
        for i in rcskel:
           f.write(i)
           f.write('\n')
        f.close()
        #fills the gui with default values
        self.conf = self.loadRcFile('.epigrassrc')
        self.fillGui(self.conf)
        os.chdir(self.curdir)
    
    def updateRc(self):
        """
        Updates the epigrassrc file with the contents of the configuration
        dictionary.
        """
        usern = pwd.getpwuid(os.getuid())[0] #Get the user name
        os.chdir('/home/'+usern)
        if os.access('.epigrassrc',os.F_OK):
            os.system('rm .epigrassrc')
            os.system('touch .epigrassrc')
        f = open('.epigrassrc','w')
        
        rcskel = ['#EpiGrass Configuration File',
            '[model]',
            'script=%s'%self.conf['model.script'],
            '[database]',
            'backend=%s'%self.conf['database.backend'],
            'host=%s'%self.conf['database.host'],
            'port=%s'%self.conf['database.port'],
            'user=%s'%self.conf['database.user'],
            '[settings]',
            'name=%s'%self.conf['settings.name'],
            'editor=%s'%self.conf['settings.editor'],
            'pdfviewer=%s'%self.conf['settings.pdfviewer'],
            'language=%s'%self.conf['settings.language']
            ]
        for i in rcskel:
           f.write(i)
           f.write('\n')
        f.close()
        os.chdir(self.curdir)
    
    
    def loadRcFile(self,fname,config={}):
        """
        Loads epigrassrc.
        Returns a dictionary with keys of the form
        <section>.<option> and the corresponding values.
        """
        config = config.copy()
        cp =ConfigParser.SafeConfigParser()
        cp.read(fname)
        for sec in cp.sections():
            name =  string.lower(sec)
            for opt in cp.options(sec):
                config[name+"."+string.lower(opt)] = string.strip(cp.get(sec,opt))
        os.chdir(self.curdir)
        return config
        
    def fillGui(self,conf):
        """
        Fill the gui fields from configuration dictionary conf.
        """
        if self.conf['settings.language'] == 'pt_BR':
            self.langCombo.setCurrentItem(1)
        elif self.conf['settings.language'] == 'fr':
            self.langCombo.setCurrentItem(2)
        else:
            self.langCombo.setCurrentItem(0)
        try:
            self.scriptNameEdit.setText(conf['model.script'])
            self.hostnEdit.setText(conf['database.host'])
            self.portEdit.setText(conf['database.port'])
            self.uidEdit.setText(conf['database.user'])
            self.unameEdit.setText(conf['settings.name'])
            self.editorEdit.setText(conf['settings.editor'])
            self.pdfEdit.setText(conf['settings.pdfviewer'])
        except KeyError, v:
            V = v.__str__().split('.')
            QMessageBox.information(None,
                self.trUtf8("Syntax Error"),
                self.trUtf8("""Please check file .epigrassrc for missing %s keyword
                from section %s """%(V[1],V[0])),
                None,
                None,
                None,
                0, -1)
##            usern = pwd.getpwuid(os.getuid())[0] #Get the user name
##            os.system('rm /home/'+usern+'.epigrassrc')
##            self.initRc()

    def checkConf(self):
        """
        Check if the configuration dictionary is complete
        """
        if not self.conf:
            self.initRc()
        for i in self.conf.items():
            if not i[1]:
                QMessageBox.information(None,
                    self.trUtf8("Incomplete Configuration"),
                    self.trUtf8("""Please enter a value for %s."""%i[0]),
                    self.trUtf8("&OK"),
                    None,
                    None,
                    0, -1)
                return 0
        return 1

        
    def editScript(self):
        """
        Opens the model script with the user's preferred editor.
        """
        if self.editorEdit.text() and self.scriptNameEdit.text():
            ed = str(self.editorEdit.text())
            scr = str(self.scriptNameEdit.text())
            os.system('%s %s'%(ed,scr))
        else:
            QMessageBox.warning(None,
                self.trUtf8("Editor or Script not selected"),
                self.trUtf8("""Please make sure you have selected both
an editor and your model's script."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)

        
        
    def chooseScript(self):
        """
        starts the file selction dialog for the script.
        """
        scrname = QFileDialog.getOpenFileName(\
                    QString.null,
                    self.trUtf8("*.epg"),
                    None, None,
                    self.trUtf8("Select your Model's Script"),
                    None, 1)
        self.scriptNameEdit.setText(scrname)
        self.conf['model.script'] = scrname
    
    def readGui(self):
        """
        Gets the info from the GUI into the configuration dictionary.
        """
        self.conf['model.script'] = str(self.scriptNameEdit.text())
        self.conf['database.host'] = str(self.hostnEdit.text())
        self.conf['database.port'] = int(str(self.portEdit.text()))
        self.conf['database.user'] = str(self.uidEdit.text())
        self.conf['database.backend']= str(self.dbType.currentText()).lower()
        self.conf['settings.name'] = unicode(str(self.unameEdit.text()))
        self.conf['settings.editor'] = str(self.editorEdit.text())
        self.conf['settings.pdfviewer'] = str(self.pdfEdit.text())
        
        os.chdir(os.path.split(self.conf['model.script'])[0])
        print os.getcwd()
        
        if int(self.langCombo.currentItem()) == 1:
            self.conf['settings.language'] = 'pt_BR'
        elif int(self.langCombo.currentItem()) == 2:
            self.conf['settings.language'] = 'fr'
        else:
            self.conf['settings.language'] = 'en'

    def onRunFuture(self):
        """
        Run the simulation on a separate thread
        """
        return Future(self.onRun)
    def onRun(self):
        """
        starts the simulation when the run button is pressed
        """
        self.tabWidget.setCurrentPage(2)
        app.processEvents(1000)
        self.readGui()
        self.updateRc()
        if self.checkConf():
            if not self.dbType.currentItem():
                if not self.pwEdit.text():
                    QMessageBox.warning(None,
                        self.trUtf8("Missing Database Password"),
                        self.trUtf8("""Please enter password for the Mysql Database."""),
                        QString.null,
                        QString.null,
                        QString.null,
                        0, -1)
                    return
                    
            self.sim = S = simulate(fname=self.conf['model.script'],host=self.conf['database.host'],port=int(self.conf['database.port']),
                        db='epigrass',user=self.conf['database.user'], password=str(self.pwEdit.text()),backend=str(self.dbType.currentText()))
            S.gui = self
            if not S.replicas:
                S.start()
                app.processEvents(1000)
                dot = spread.Spread(self.sim.g, self.sim.outdir,self.sim.encoding)
                if S.Rep:
                    rep = Rp.report(S)
                    self.textEdit1.insertParagraph('Report generation started.',-1)
                    app.processEvents(1000)
                    rep.Assemble(S.Rep)
            else: #Repeated runs 
                self.repRuns(S)
                
            
            # In case of a batch
            if S.Batch:
                self.textEdit1.insertParagraph('Simulation Started.',-1)
                app.processEvents(1000)
                # run the batch list
                for i in S.Batch:
                    #Makes sure it comes back to original directory before opening models in the batch list
                    os.chdir(self.sim.dir)
                    # Generates the simulation object        
                    self.sim = T = simulate(fname=i,host=self.conf['database.host'],port=int(self.conf['database.port']),
                        db='epigrass',user=self.conf['database.user'], password=str(self.pwEdit.text()),backend=str(self.dbType.currentText()))
                    T.gui = self
                    print 'starting model %s'%i
                    T.start()  # Start the simulation 
                    app.processEvents(1000)
                    if S.Rep: #Start report generation
                        rep = Rp.report(T)
                        self.textEdit1.insertParagraph('Report generation started.',-1)
                        app.processEvents(1000)
                        rep.Assemble(S.Rep)

            self.textEdit1.insertParagraph('Done!',-1)
            #print 'Agora...'
            #spdisp = spread.Spread(self.sim.g)
            #spdisp.display()
        else:
            return
    
    def repRuns(self,S):
        """
        Do repeated runs
        """
        if S.randomize_seeds:
            randseed = 1
        else:
            randseed = 0
        seeds = S.randomizeSeed()
        for i in range(S.replicas):
            print "Starting replica number %s"%i
            self.textEdit1.insertParagraph("Starting replica number %s"%i,-1)
            self.sim = S = simulate(fname=self.conf['model.script'],host=self.conf['database.host'],port=int(self.conf['database.port']),
                db='epigrass',user=self.conf['database.user'], password=str(self.pwEdit.text()),backend=str(self.dbType.currentText()))
            if randseed:
                S.setSeed(seeds[i])
            S.round = i
            S.start()
            app.processEvents(1000)
            if S.Rep: #Generate report if necessary
                rep = Rp.report(S)
                self.textEdit1.insertParagraph('Report generation started.',-1)
                app.processEvents(1000)
                rep.Assemble(S.Rep)
    
    def onDbBackup(self):
        """
        Dumps the epigrass databse to an sql file.
        """
        if self.conf['database.host'] !='localhost':
            QMessageBox.warning(None,
                self.trUtf8("Non-local Database Server"),
                self.trUtf8("""Currently, the database backup function only
                works on local database servers."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)


        os.system('mysqldump -u %s -p%s --opt epigrass > epigrass.sql'%(str(self.uidEdit.text()),self.pwEdit.text()))
        
        QMessageBox.information(None,
            self.trUtf8("Restore Instructions:"),
            self.trUtf8("""The epigrass database has been Backed up
to a file named "epigrass.sql".
This file is in you current working directory.
To restore the database type:
epigrass.sql > mysql"""),
            self.trUtf8("&OK"),
            None,
            None,
            0, -1)
    
    def onDbInfo(self):
        pass
    
    def onHelp(self):
        """
        Opens the userguide
        """
        ab = aboutDialog()
        ab.show()
        ab.exec_loop()
        if os.path.exists('/usr/share/epigrass/docs/userguide.pdf'):
            try:
                os.system('%s /usr/share/epigrass/docs/userguide.pdf'%str(self.pdfEdit.text()))
            except:
                QMessageBox.warning(None,
                    self.trUtf8("Help not available"),
                    self.trUtf8("""Could not open user guide.
    Please make sure your chosen PDF viewer is installed."""),
                    self.trUtf8("&OK"),
                    None,
                    None,
                    0, -1)

    def onRepOpen(self):
        """
        Opens the report PDF
        """
        
        out = commands.getstatusoutput('%s %s'%(self.conf['settings.pdfviewer'],self.sim.repname))
        if out[0] != 0:
            QMessageBox.warning(None,
                self.trUtf8("No Report"),
                self.trUtf8("""Could not open the report.
Make sure you have generated it."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)
            
    
    def onVisual(self):
        """
        Scan the epigrass database an shows available simulations.
        """
        if not self.dbType.currentItem():
            if not self.pwEdit.text():
                QMessageBox.warning(None,
                    self.trUtf8("Missing Database Password"),
                    self.trUtf8("""Please enter the password for the Epigrass database in the first tab."""),
                    self.trUtf8("&OK"),
                    QString.null,
                    QString.null,
                    0, -1)
                return
        self.Display=epi.viewer(host=str(self.hostnEdit.text()),port=int(str(self.portEdit.text())),
                        db='epigrass',user=str(self.uidEdit.text()), pw=str(self.pwEdit.text()),backend=self.conf['database.backend'])
        for s in self.Display.tables:
            if not s.startswith('adj_'):
                self.tableList.insertItem(s)
        #check for available maps
        maplist = [i for i in os.listdir(os.getcwd()) if i.endswith('.map')]
        for m in maplist:
            self.mapList.insertItem(m)
    
    def getVariables(self):
        """
        Fill the variables list whenever a table is selected in the table list
        """
        self.variableList.clear()
        table = str(self.tableList.currentText())
        self.vars = self.Display.getFields(table)
        for s in self.vars:
            if s not in ['id','name','geocode','lat','longit','time']:
                self.variableList.insertItem(s)
    
    def onPlayButton(self):
        """
        Calls the epiplay module to replay the epidemic from a database table.
        """
        #get variable to animate and its position in the database
        var = str(self.variableList.currentText())
        pos = self.vars.index(var)
        r = self.rateSpinBox.value() 
        table = str(self.tableList.currentText())
        mapa = str(self.mapList.currentText())
        modname = table.split('_')[0] #self.sim.modelName.split('/')[-1]
        nodes,am = self.Display.readNodes(modname, table)
        if not nodes:
            QMessageBox.warning(None,
                self.trUtf8("Empty Table"),
                self.trUtf8("""You have selected an empty table.
Please select another table from the menu."""),
                QString.null,
                QString.null,
                QString.null,
                0, -1)
            return

        numbnodes = len(nodes)
        data = self.Display.readData(table)
        edata = self.Display.readEdges(table)
        numbsteps = len(data)/numbnodes
        self.Display.viewGraph(nodes,am,var,mapa)
        self.Display.anim(data,edata,numbsteps,pos,r)
        #Future(self.Display.keyin,data,edata,numbsteps,pos,r)
        self.Display.keyin(data,edata,numbsteps,pos,r)
    
    def onConsensus(self):
        """
        Build the consensus tree
        """

        modelpath = os.path.split(self.conf['model.script'])[0]
        print type(modelpath)

        path = QFileDialog.getExistingDirectory(\
            self.trUtf8(modelpath),
            None, None,
            self.trUtf8("Select Directory with Tree Files (epipath*.csv)"),
            1, 1)
        cutoff = QInputDialog.getDouble(\
            self.trUtf8("Branch Support"),
            self.trUtf8("Enter minimum branch support level to display:"),
            50.0, 0.0, 100.0, 1)
        cons = spread.Consensus(str(path),cutoff)

    
    def setBackend(self):
        """
        activate/deactivate db spec groupbox
        """
        self.backend = self.conf['database.backend']= str(self.dbType.currentText()).lower()
        #print self.backend
        if self.dbType.currentItem():
            self.dbSpecGroupBox.setEnabled(0)
            self.dbBackup.setEnabled(0)
        else:
            self.dbSpecGroupBox.setEnabled(1)
            self.dbBackup.setEnabled(1)
    
    def onExit(self):
        """
        Close the gui
        """
        if self.sim:
            if self.sim.g.gr:
                self.sim.g.clearVisual()
        self.close()
        
class Future:
    """
    By David Perry - http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/84317
    To run a function in a separate thread, simply put it in a Future:

    >>> A=Future(longRunningFunction, arg1, arg2 ...)

    It will continue on its merry way until you need the result of your function. 
    You can read the result by calling the Future like a function, for example:

    >>> print A()

    If the Future has completed executing, the call returns immediately. 
    If it is still running, then the call blocks until the function completes. 
    The result of the function is stored in the Future, so subsequent calls to 
    it return immediately.

    A few caveats:
    Since one wouldn't expect to be able to change the result of a function, 
    Futures are not meant to be mutable. This is enforced by requiring the 
    Future to be "called", rather than directly reading __result. If desired, 
    stronger enforcement of this rule can be achieved by playing 
    with __getattr__ and __setattr__.

    The Future only runs the function once, no matter how many times you 
    read it. You will have to re-create the Future if you want to re-run your 
    function; for example, if the function is sensitive to the time of day.

    For more information on Futures, and other useful parallel programming 
    constructs, read Gregory V. Wilson's _Practical Parallel Programming_.
    """
    def __init__(self,func,*param):
        # Constructor
        self.__done=0
        self.__result=None
        self.__status='working'

        self.__C=Condition()   # Notify on this Condition when result is ready

        # Run the actual function in a separate thread
        self.__T=Thread(target=self.Wrapper,args=(func,param))
        self.__T.setName("FutureThread")
        self.__T.start()

    def __repr__(self):
        return '<Future at '+hex(id(self))+':'+self.__status+'>'

    def __call__(self):
        self.__C.acquire()
        while self.__done==0:
            self.__C.wait()
        self.__C.release()
        # We deepcopy __result to prevent accidental tampering with it.
        a=copy.deepcopy(self.__result)
        return a

    def Wrapper(self, func, param):
        # Run the actual function, and let us housekeep around it
        self.__C.acquire()
        try:
            self.__result=func(*param)
        except:
            self.__result="Exception raised within Future"
        self.__done=1
        self.__status=`self.__result`
        self.__C.notify()
        self.__C.release()

def loadLang(app,tr,lang):
    """
    loads the language based on the user's choice.
    """
    if lang == 'pt_BR':
        tr.load('manager_pt_BR','.')
        app.installTranslator(tr)
    if lang == 'fr':
        tr.load('epigrass_fr','.')
        app.installTranslator(tr)
    else:
        pass
        
def main():
    global app
    app = QApplication(sys.argv)
    QObject.connect(app,SIGNAL("lastWindowClosed()"),app,SLOT("quit()"))
    w = MainPanel_Impl()
    app.setMainWidget(w)
    w.show()
    app.exec_loop()

if __name__ == "__main__":
    main()
##    app = QApplication(sys.argv)
##    QObject.connect(app,SIGNAL("lastWindowClosed()"),app,SLOT("quit()"))
##    w = MainPanel_Impl()
##    app.setMainWidget(w)
##    w.show()
##    app.exec_loop()
