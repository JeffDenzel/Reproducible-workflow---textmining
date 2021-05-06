# A reproducible research workflow using JSON parsing and text mining in Python and analysis using R.



The main aim of this repository is to have a clean and basic structure, which can be easily adjusted to use in an actual project. In this project, the following is done:
- Pipeline stage "data-preparation"
  - Download raw JSON data in a zip file
The readme for this data is available at: Tweets Coronavirus White House Press Briefing (USA)
https://uvt-public.s3.eu-central-1.amazonaws.com/data/rsm2020/team13_covid19_briefing_usa.txt
The data is available at: https://uvt-public.s3.eu-central-1.amazonaws.com/data/rsm2020/team13_covid19_briefing_usa.zip
  - Unzip data
  - Parse JSON data to CSV file
  - Load CSV file, and enrich textual data with text mining metrics using Python's TextBlob package for sentiment analysis and google's translator API to change tweets to english.
- Pipeline stage "analysis"
  - Load final output file from previous pipeline stage, run precleaning code
  - Produce RMarkdown HTML output with simple statistics (Correlation table, Scatterplot with a best fit line and Histograms)
  
## Dependencies
- Python via the Anaconda distribution
- TextBlob via `pip install -U textblob`
- NLTK dictionaries; open Python, then type
  ```
  import nltk
  nltk.download('punkt')
  ```
  
- Gnu Make
- Vader sentiment analyser via 
- R and the following packages:

```
install.packages(c("stargazer", "knitr", "data.table", "ggplot2","corrr","dplyr"))
```

Detailed installation instructions can be found here: [tilburgsciencehub.com/tutorial](http://tilburgsciencehub.com/tutorial)
