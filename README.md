# Housing Price Analysis in Major Indian Cities

## Project Description

This project aims to create an automated data pipeline for collecting, processing, storing, and visualizing housing price data from major Indian cities (Hyderabad, New Delhi, Bangalore, Kolkata, Chennai). The project leverages various tools and technologies to achieve a robust and scalable data analytics solution.

## Table of Contents
- [Project Description](#project-description)
- [Table of Contents](#table-of-contents)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [Data Collection](#data-collection)
- [Data Processing](#data-processing)
- [Data Visualization](#data-visualization)
- [Automation and Deployment](#automation-and-deployment)
- [Business Questions](#business-questions)

## Technologies Used
- **Scrapy**: For web scraping and data collection.
- **MongoDB**: For storing fetched data.
- **Python (Pandas, NumPy)**: For data processing and transformation.
- **Power BI**: For data visualization and dashboard creation.
- **Power BI Server**: For deploying and sharing dashboards.
- **Apache Airflow**: For automating the data collection and processing pipeline.
- **GitHub**: For version control.
- **AWS and Docker**: For deployment and scalability.

## Project Setup

### Prerequisities
 - Python 3.x
 - Virtual environment setup

### Installation Setup

1. **Clone the Repository**
    ```sh
        git clone https://github.com/Nikhilreddy447/house_price_analysis.git
        cd house_price_analysis
    ```
2. **Create and Activate Virtual Environment**
    ```sh
        # On Windows
        python -m venv venv
        venv\Scripts\activate

        # On macOS/Linux
        python -m venv venv
        source venv/bin/activate
    ```
3. **Install Dependencies**
    ```sh
        pip install -r requirements.txt
    ```

[Table Content](#table-of-contents)

## Data Collection 
### Command to start scrapy project

```sh
scrapy startproject dataCollection
```

### Command to generate spider

```sh
scrapy genspider dataacollector www.magicbricks.com
```

### Scrapy Spider
The Scrapy spider collects house price data from MagicBricks. The data includes fields such as city, locality name, coordinates, price, and more.

### Steps to Run the Spider
1. **Define the Item**: The item defines the structure of the scraped data.
2. **Update the Spider**: The spider collects data and yields items.
3. **Create the Pipeline**: The pipeline processes and saves the data.
4. **Enable the Pipeline**: Enable the pipeline in the Scrapy settings.
5. **Run the Spider**: Use the Scrapy command to run the spider and collect data.

### Running the Spider
```sh
scrapy crawl data_collector
```

[Table Content](#table-of-contents)


## Business Questions

This project aims to address the following key questions and provide valuable insights for stakeholders in the real estate industry:

1. How does the average housing price vary across different cities in our dataset, and what factors contribute most significantly to these price variations?
2. Can you identify any trends or patterns in luxury property listings versus non-luxury listings, and how does this impact market demand and pricing?
3. What is the distribution of property sizes (in terms of square footage) across different localities, and is there a correlation between property size and listing price?
4. Are there any notable differences in pricing trends between furnished and unfurnished properties, and how does this affect buyer preferences?
5. Can you provide insights into the demand for properties with specific amenities such as parking spaces, power backup, or nearby schools, and how does this influence property values?
6. What is the average time properties stay on the market before being sold or rented, and are there any seasonal fluctuations or regional variations in this metric?
7. Are there any particular neighborhoods or localities experiencing rapid growth in property prices, and what factors are driving this growth?
8. Can you analyze the impact of recent regulatory changes or economic trends on the housing market, such as changes in interest rates or government policies?
9. How do the preferences of tenants vary across different cities or property types, and what amenities or features are most sought after by renters?
10. Based on historical data, can you forecast future housing price trends for the coming months or years, considering factors like market demand, economic indicators, and demographic shifts?

These questions delve into various aspects of the dataset, including pricing dynamics, market trends, buyer preferences, regulatory influences, and predictive analytics, providing valuable insights that can guide strategic decision-making for stakeholders in the real estate industry.

[Table Content](#table-of-contents)

---
