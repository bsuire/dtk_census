# dtk_census

A Django/AngularJS app that displays aggregates from the US census database.

### Installation

I have uploaded a script to automatically install and run the application: install.sh, available in the root repository.

1. Download census database from http://dev.dataiku.com/~cstenac/dev-recruiting/us-census.db.gz.
2. Unzip and place in the folder where you wish to install the app.
2. Copy the install script install.sh and place it in the same folder as the census database.
3. Open up a terminal and run: 
   `sh install.sh`
4. The following message should appear, meaning the installation was successful and the app is live:
```
Starting development server at http://127.0.0.1:8000/   
Quit the server with CONTROL-C.
```

Now you can start using the app at http://127.0.0.1:8000/.
