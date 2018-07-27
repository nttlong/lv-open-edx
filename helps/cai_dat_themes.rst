
HƯỚNG DẪN CÀI ĐẶT THEMES
----------------------------




sudo chown -R daemon:daemon $PATH/apps/edx/var/themes/THEME_NAME/

cd /opt/bitnami/apps/edx/bin

sudo ./paver.edxapp update_assets lms --settings=aws

sudo ./paver.edxapp update_assets cms --settings=aws


Trong ca 2 file lms.env.json va cms.env.json:

     "COMPREHENSIVE_THEME_DIRS": [

         "installdir/apps/edx/var/themes/"

     ],

     "ENABLE_COMPREHENSIVE_THEMING": true,

     "FEATURES": {

         ...
         "USE_CUSTOM_THEME": true

     },

     "THEME_NAME": "my-custom-theme"


How to apply a custom theme?
