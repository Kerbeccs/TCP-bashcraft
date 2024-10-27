# TCP-bashcraft
Okey so I have successfully created a TCP connection which when reads amessage "hi server "a outputs it and closes connection
If you want to test it , copy it as it is .
Please dont misplace any file.
open new terminal write this command "python manage.py runserver"
something like this will appear  ->''
""TCP Server started on 127.0.0.1:8080
TCP Server started on 127.0.0.1:8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 27, 2024 - 22:20:16
Django version 4.1.13, using settings 'tcp_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.""


Then do ctrl+shift+`  ->`(tick below escape button) anew terminal will open write these 2 commands-> cd path/to/your/tcp_app (change the back slashes in the path otherwise it wont work) the write the commnad "python client.py"......

now just switch between both terminal you will see the ouput in both of client and server side
