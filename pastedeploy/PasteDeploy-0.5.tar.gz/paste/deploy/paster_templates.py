import os
from paste.script.templates import Template

class PasteDeploy(Template):

    _template_dir = 'paster_templates/paste_deploy'
    summary = "A web application deployed through paste.deploy"
    
    egg_plugins = ['PasteDeploy']
    
    required_templates = ['PasteScript#basic_package']

    def post(self, command, output_dir, vars):
        for prereq in ['PasteDeploy']:
            command.insert_into_file(
                os.path.join(output_dir, 'setup.py'),
                'Extra requirements',
                '%r,\n' % prereq,
                indent=True)
        command.insert_into_file(
            os.path.join(output_dir, 'setup.py'),
            'Entry points',
            ('      [paste.app_factory]\n'
             '      main = %(package)s.wsgiapp:make_app\n') % vars,
            indent=False)
        if command.verbose:
            print '*'*72
            print '* Run "paster serve docs/devel_config.ini" to run the sample application'
            print '* on http://localhost:8080'
            print '*'*72
        
