# chrome_extract

small utility script meant to extract chrome folders from https://google-chrome.en.uptodown.com/windows installers.

## usage:

place installers in the same directory as the script and run it.

````markdown
- chrome_extract.py
- google-chrome-151-0-7922-72.msi
- google-chrome-151.0-7922-138.msi
- google-chrome-135-0-7049-42.exe
- google-chrome-133-0-6943-60.zip
- ...
````
will extract to:

````markdown
- 151.0.7922.72/
- 151.0.7922.138/
- 135.0.7049-42/
- 133.0.6943-60/
- ...
- chrome_extract.py
- google-chrome-151-0-7922-72.msi
- google-chrome-151.0-7922-138.msi
- google-chrome-135-0-7049-42.exe
- google-chrome-133-0-6943-60.zip
- ...
````
`uptodown.com` hosts its chrome version in three forms (.zip, .msi and .exe). chrome_extract supports all of them.
