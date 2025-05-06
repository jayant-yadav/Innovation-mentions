# UNICEF Innovation Mentions

This application processes UNICEF public End Year Summary Narratives (EYSN) and analyzes mentions of Innovation throughout the corpus.

## source for EYSN:  
[EYSN](https://insight.unicef.org/apps01/mgtrep/_layouts/15/ReportServer/RSViewerPage.aspx?rv:RelativeReportUrl=/apps01/mgtrep/Reports/RAM3%20End-Year%20Summary%20Narrative%20Analysis.rdl&rv:HeaderArea=none&authToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im1FQnlFcUg4YXRrT0J2aU9fR0pvQ0FENy1qayJ9.eyJhdWQiOiJ1cm46QXBwUHJveHk6Y29tIiwiaXNzIjoiaHR0cDovL2xvZ2luLnVuaWNlZi5vcmcvYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTY5NTc0MTUwNCwiZXhwIjoxNjk1NzQ1MTA0LCJyZWx5aW5ncGFydHl0cnVzdGlkIjoiMTMzZGE0MzAtOWE2MS1lNzExLTgwZmQtMDA1MDU2ODQ1NzIyIiwidXBuIjoianlhZGF2QHVuaWNlZi5vcmciLCJjbGllbnRyZXFpZCI6IjNkY2U3MGYxLWRjNjYtMDAwMi0zOWQyLWZiM2Q2NmRjZDkwMSIsImF1dGhtZXRob2QiOiJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YWM6Y2xhc3NlczpQYXNzd29yZFByb3RlY3RlZFRyYW5zcG9ydCIsImF1dGhfdGltZSI6IjIwMjMtMDktMjZUMTM6MDc6NTguOTE2WiIsInZlciI6IjEuMCJ9.T8RX_woWo70c4udWuiXXfI4jTV6ut3dan5pHgW0vbbsrj861AZsZ1LHmS9cXh2E1K4NRB_81hSvovtRVnbXeA5ORrvdUYXkpinZcnCX1O5dJLTjgZ9kRI_6ckietIoffjLkwJN8s0Qj2emoxqZVgGtIbUt6AUX2f5QIecP1tC0c2Gni3Fis8fZHeRro2ZEapyFH3_q5DoFZE-JFkV2Try9HL6_v2jvLr17ba-nuPRRP8GHWfLUAJJZylcAyINH0XBH-M0sObWR4dsfEKLX5r8EB0AtwRA7vrxSe9-KE8roaqYdpJFXs4m2RCLr1JbfRabxZQzg20ehB2qGFyn3I67Q&client-request-id=3dce70f1-dc66-0002-39d2-fb3d66dcd901)

## Adding a New End Year Summary Narrative (EYSN)
1. Download EYSN report from above source link in CSV(comma delimited) format. Select all regions, select year, select all sections.
2. Rename the downloaded file with year appended in its name. "RAM3 End-Year Summary Narrative Analysis.csv" -> "RAM3 End-Year Summary Narrative Analysis 2024.csv".
3. Upload the file to the `public` folder.
4. Update the `listing.json` file by adding the name of the uploaded file. Make sure that it is a valid json format.
5. Visit https://jayant-yadav.github.io/Innovation-mentions/
6. Download the processed file by clicking "Download CSV" button.
7. Rename the file to "innovation_mentions.xlsx" and upload it to [COAR analysis folder](https://unicef.sharepoint.com/teams/OOI-A2S/DocumentLibrary1/Forms/AllItems.aspx?id=%2Fteams%2FOOI%2DA2S%2FDocumentLibrary1%2F8%2E%20Evidence%2FOOI%20level%2FCOAR%20analysis&viewid=30cf7b5a%2D275a%2D47e4%2Daaf9%2Dc38cf1fe9fe6).

## Searching with Keywords
To search using multiple keywords, use the `|` symbol to separate them.
