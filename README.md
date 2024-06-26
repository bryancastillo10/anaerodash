<img src="utility/images/banner.png">
<h3 align="center">A Dedicated Web App for AD System Evaluation</h3>

![Static Badge](https://img.shields.io/badge/AnaeroDash-v_1.1-darkgreen)
![Static Badge](https://img.shields.io/badge/Python_3.10.12-%233776AB?style=plastic&logo=python&logoColor=%23E6DB3D&labelColor=%230072B2&color=%23757979)

## Tools Used

![Static Badge](https://img.shields.io/badge/Streamlit-%23FF4B4B?style=for-the-badge&logo=streamlit&logoColor=%23D55E00&labelColor=%23000000&color=%23868181)
![Static Badge](https://img.shields.io/badge/DuckDB-duckdb?style=for-the-badge&logo=duckdb&logoColor=%23F0E442&labelColor=%23000000&color=%23868181)
![Static Badge](https://img.shields.io/badge/Plotly-%233F4F75?style=for-the-badge&logo=plotly&logoColor=%2356B4E9&labelColor=%23000000&color=%23868181)

![Static Badge](https://img.shields.io/badge/HTML-html5?style=for-the-badge&logo=css3&logoColor=%23E69F00&labelColor=%23000000&color=%23868181)
![Static Badge](https://img.shields.io/badge/CSS-%231572B6?style=for-the-badge&logo=css3&logoColor=%2378CAF9&labelColor=%23000000&color=%23868181)

---

## Description

> Anaerobic Digestion Treatment presents a possibility for sustainability, which has emerged as a primary objective in the field of environmental science and engineering. By offering a quick and dependable data analysis and visualization in the AD process, this APP can support our fellow environmentalists in their advocacy for a sustainable environment.

### Demo

![Alt text](utility/images/demo.png)

---

### Usage

---

1. Streamlit Community Cloud

   **Website Link:** [AnaeroDash](https://anaerodash.streamlit.app/)

   **Username:** public_user

   **Password:** abc123

---

2.  Cloning GitHub Repository

    Step 1: Clone this repository and then open your command line in the project directory.

    Step 2: Create and activate your virtual environment.
    Take note that env_name can be changed depending on the name of virtual environment you want.

    ```console
        python3 -m -venv env_name
    ```

    For Windows:

    ```
        env_name\Scripts\activate
    ```

    For MacOS/Linux Ubuntu:

    ```
        env_name/bin/activate
    ```

    Step 3: Install those libraries used in this project.Overall, the libraries currently used were streamlit for the web framework, streamlit-authenticator for the authentication system, duckdb for data handling and calculations, and plotly for the interactive data visualization.

    ```
         pip install streamlit streamlit-authenticator duckdb plotly
    ```

    Step 4: Run the main Python script.

    ```
           streamlit run 1_📊_Dashboard.py
    ```

    Click on the link provided for the local host browser. Use the same account provided.

    **Username:** public_user

    **Password:** abc123

### Key Features

1. Dashboard Application (To instantly visualize and provide additional insights to the user about their AD system based on the uploaded .csv file
2. Create your Dataset (It is available on the app an online table editor to create your own dataset to be analyzed in this app. It should be noted to strictly follow the guidelines provided in the APP for effective processing)
3. Internationalization (Since the developer currently lives in Taiwan, he added some feature of providing the APP in Chinese(Traditional) version for the convenience of local viewers/users in Taiwan. )

### Future Plan

A Machine Learning Algorithm (such as Random Forest Classifier/Support Vector Machine/Reccurent Neural Network/ or any similar models) may be incoroporated to the APP for the prediction of Biogas production which is an important operational parameter of the system. Those predictions could provide some insights to the continuous operation of the AD system.
