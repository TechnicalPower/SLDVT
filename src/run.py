import voice_translate
import ui
## Instead of change docker file for application running, change this file.


## starts with running default 
var_run = input("PICK WORKFLOW || voice : '1' || ui(main) : '2'")
if(var_run == "1"):
    voice_translate.main()
elif(var_run == "2"):
    ui