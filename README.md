# QnA Spirits Book

## Teste

-download the code

-open project

-create and active a virtual environment

      ---virtual environment on python

      python3 -m venv .venv


      ---virtual environment activation on Linux

      source .venv/bin/activate


      ---virtual environment activation on Windows

      .venv\Scripts\activate.bat


-install requeriments
```
pip install -r requirements.txt
``` 

-go to apps folder 
```
cd ~/kardecbooks/spiritsbook
```  

-Using mysql database on localhost named 'questions_answers'. Note: you might need to change the databases settings

        path: spiritsbook/spiritsbook/settings/base.py
        
        current > mysql://root:@127.0.0.1:3306/questions_answers
        
        pattern > mssql://USER:PASSWORD@HOST:PORT/NAME
                

-Run local server
```
python manage.py runserver
```
