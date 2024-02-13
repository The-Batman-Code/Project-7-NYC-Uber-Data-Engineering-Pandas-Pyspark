# Project-7-NYC-Uber-Data-Engineering

![](Images/Data-Flow.png)


# Introduction - 
This Data Analytics/Data Engineering project involves normalizing/denormalizing existing data for various purposes. I have already created a data model and visualized it. The transformation steps needed for establishing the data model have been completed using Pandas and Mage. Analytical queries using SQL on BigQuery have been written. Employing SQL joins, I have denormalized the data essential for our dashboard. The final step involves creating our analytics dashboard.

# Tech stack used - 
1. Python - Used the famous Pandas library
2. Jupyter Notebook in VS Code as my Code Editor
3. Lucid Chart to visualize the Data Model
4. Google Cloud Storage
5. Google Cloud's Bigquery
6. Google Cloud's Compute Engine
7. Looker Studio

# How to deploy it yourself? 👇
1. Clone this repository and place it in your working directory.
2. Run the analytics.ipynb file and it will create your fact and dimension tables as shown in the data model diagram below.
![](Images/Data-Model.png)

3. Now the local work is done, it's time to move to Google Cloud Platform🍻.
4. In the Google Cloud Console create a VM under the Compute Engine section with the following configruations-
![](Images/Config-1.png)

![](Images/Config-2.png)

![](Images/Config-3.png)

![](Images/Config-4.png)

![](Images/Config-5.png)

5. After the VM is up and running, SSH into it and run the following commands -
```
sudo apt-get update
sudo apt install python3-pip
pip install google-cloud-aiplatform
pip install mage-ai
```
6. Now give the VM a restart by stopping and starting it.
7. Again SSH into it and enter the following command -
```
mage start <YOUR-PROJECT-NAME>
```
8. You will see the following in your SSH terminal.
![](Images/SSH-Terminal-Mage.png)

9. Now open a new tab in your browser and put the following link -
```
<YOUR-VM-EXTERNAL-IP>:6789
```
10. The link won't work... hahah... Bummer!!! Let's get it to work.
11. In the internal IP section of your VM, click on the 'nic0' link.
12. You will get redirected to Network Interface details section. on the left panel click on the firewall section.
13. In the upper panel click on the 'Create Firewall Rule'.
14. Enter the following settings -

![](Images/Mage-Access-1.png)

![](Images/Mage-Access-2.png)

![](Images/Mage-Access-3.png)

16. Now click on create. You should now be able to access Mage from the same link you used earlier in step 9.
17. You will see the Mage UI like below. Click on the 'New' button, then click on Standard(batch) button.
18. Click on the 'Data Loader' button -> 'Python' -> 'API'.
19. Give it a name and click on 'Save and add'.
20. Now we need the link to our csv data to put it in the code so create a bucket in google cloud storage, make it public and put it's link in the 'Data-Loader.py' file in the mage folder.
21. Paste the code in the 'Data Loader' section in Mage.
22. Now below the 'Data Loader' section, click on the 'Transformer' button -> Python -> Generic(no template).
23. Paste the code from 'transformation.py' file in the mage folder.
24. Now click on the 'Data Exporter' button below the 'Transformer' code and paste the code in 'Data-Exporter.py' file in the mage folder.
25. To be able to export data into Bigquery we need a Service Account. Create a service account and put it's credentials in the 'io_config.yaml' file in Mage.

![](Images/Config-gcp.png)

![](Images/Config-gcp-2.png)

26. Now after the credentials are set, create a dataset in Bigquery and paste it's information accordingly in the 'Data-Exporter.py' code. Now run each cell of loader, transformation and exporter. You will get your data loaded in Bigquery like this.

![](Images/Bigquery.png)

# Extra - 
1. Now you can run some analytical SQL queries like the ones shown below -

![](Images/SQL-1.png)

![](Images/SQL-2.png)

2. Now we can also utilize Bigquery to build a Dasboard, but to do so we need a table which has all the columns we need to make it. In order to do that we run the following SQL query - 

![](Images/all-table.png)

3. We can make a dashboard like the one below -

![](Images/dashboard-1.png)

![](Images/dashboard-2.png)

![](Images/dashboard-3.png)














