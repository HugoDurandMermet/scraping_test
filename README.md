# SCRAPING TEST

*Applicant: Hugo Durand-Mermet*

*Date: 13/02/2022*

## Getting Started

From your global Python or virtual environment, install the necessary dependencies at the root of this folder by typing in your Shell terminal:
```Shell
pip install requirements.txt
```
Once you're all set up, you can run the script with the following command:
```Shell
python main.py --lib LIBRARY_NAME [--output CUSTOM_FILENAME]
```

The first flag of this command ```--lib``` is required; you can either use the BeautifulSoup version by typing ```BeautifulSoup``` or the Scrapy one by typing ```Scrapy```

Neither of these two choices are case sensitive, but be sure to remain careful for any mispelling error.

The second flag ```--output``` is in case you want to give a custom name for the file ouput.

Whatever you might choose, the extension will remain `.csv`.

By default, your filename will be called `drills.csv`.
