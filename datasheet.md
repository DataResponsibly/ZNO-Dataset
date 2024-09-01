**Datasheet EIE**
========

This datasheet covers both the prediction tasks we introduce and 
the underlying EIE data sources.

Motivation
----------

- **For what purpose was the dataset created?** Was there a specific task in mind? Was there a specific gap that needed to be filled? Please   provide a description.

    Creating this dataset involved:  
    - collecting of raw data about student’s performance during the standardized tests EIE (External Independent Evaluation) and NMT (National Multi-subject Test) by the Ukrainian Center for Educational Quality Assessment (UCEQA), a [budgetary institution](https://www.kmu.gov.ua/npas/27071964/) in the Ministry of Education and Science's management sphere  and about governmental expenditures on education by the Ministry of Finance;
    - cleaning, matching, and processing this raw data by our research team.

    UCEQA releases the corresponding raw data each year for two reasons:

    1. They must provide public information on their website by [Public Information Law](https://zakon.rada.gov.ua/laws/show/2939-17#Text):  
    "Public information in the form of open data is public information in a format that allows for its automated processing by electronic means, open and free access to it, and its further use.  
    Information administrators must provide public information in the form of open data upon request, publish it, and regularly update it on the unified governmental open data web portal and their websites." 
    2. They provide this information for anyone [interested in conducting independent research on the results of educational assessments.](https://zno.testportal.com.ua/opendata)

    The Ministry of Finance released the corresponding [raw data](https://mof.gov.ua/uk/the-reform-of-education) for school statistics to provide public information about expenditures on education by Public Information Law.

    **Our motivation** was to extend the dataset ecosystem available for research in two directions: the education domain and the dataset from Eastern Europe (Ukraine).

- **Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?**

    The processed dataset was created from available raw data on UCEQA and the Ministry of Finance portals by Dr. Julia Stoyanovich, Andrew Bell, and Falaah Arif Khan from the Center for Responsible AI, New York University, and Dr. Tetiana Zakharchenko, Nazarii Drushchak, Oleksandra Konopatska, and Olha Liuba from Ukrainian Catholic University.

- **Who funded the creation of the dataset?** If there is an associated grant, please provide the name of the grantor and the grant name and number.

    The collection of raw data was funded by the Ukrainian government. The cleaning, matching, and pre-processing of the raw data collected were funded by the Center for Responsible AI, New York University.

-  **Any other comments?**

    No.

Composition
-----------

- **What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?** Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.

    The datasets represent the information about the participants’ EIE (External Independent Evaluation) from 2016 to 2021 and the NMT (National Multi-subject Test) from 2022 to 2023. The test participants are those who want to use the test results to get the Certificate of Complete General Secondary Education or for admission to higher education institutions to study for a bachelor’s degree.

    There are multiple types of instances from different datasets:  
    - **Locations**: each instance represents a geographical location.  
    - **Schools**: each instance represents an organization.  
    - **School Statistics**: each instance represents an organization.  
    - **Students**: each instance represents an individual.  
    - **Students take tests**: each instance represents an individual.  
    - **Test centers**: each instance represents an organization.  
    - **Tests**: each instance represents a subject.  
    - and **Year**: each instance represents a year.

- **How many instances are there in total (of each type, if appropriate)?**

    The following table describes the sizes of the datasets

    | **Tables** | **Features** | **Datapoints** |
    | --- | --- | --- |
    | Locations | 5   | 31,862 |
    | Schools | 4   | 82,513 |
    | School Statistics | 12  | 17,636 |
    | Students | 10  | 2,490,052 |
    | Students take tests | 10  | 10,597,976 |
    | Test centers | 4   | 3,358 |
    | Tests | 2   | 25  |
    | Year | 1   | 8   |

- **Does the dataset contain all possible instances, or is it a sample (not necessarily random) of instances from a larger set?** If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances because instances were withheld or unavailable)

    The dataset contains all possible instances of students who have registered for participation in EIE or NMT in the corresponding year. Some of the collected features (name, date of birth, etc.) are hidden according to Ukraine’s law, “On Personal Data Protection."

- **What data does each instance consist of?** "Raw" data (e.g., unprocessed text or images) or features? In either case, please provide a description.

    Each instance consists of features. Appendix B of the associated paper describes each feature in the dataset.

- **Is there a label or target associated with each instance?** If so, please provide a description.

    The dataset does not have a prediction task and, therefore, has no label. However, we chose to create an associated prediction task and use the exam results as labels. There are different types of results: test status (whether an individual passed the exam), grade on the raw scale (depends on the subject and year), grade in rating score 100-200 (used for university admission), and grade іn a 12-point scale (to be used for final assessments at school).

- **Is any information missing from individual instances?** If so, please provide a description explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information but might include, e.g., redacted text.

    Some features (e.g., language of the class or raw score in Students) contain missing values. This is due to the fact that in some years, some information was not collected or published.

    |                             |                       |          |          |          |          |          |          |          |          |
    | :-------------------------: | :-------------------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
    |      **Features/Years**     |     **Table name**    | **2016** | **2017** | **2018** | **2019** | **2020** | **2021** | **2022** | **2023** |
    |        KATOTTG\_2023        |        Schools        |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |            EDRPOU           |        Schools        |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |          eotypename         |        Schools        |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |             year            |        Schools        |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |            EDRPOU           |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |            eotype           |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |           eolevel           |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |          teachstuff         |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |        nonteachstuff        |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |       teachstuffretage      |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |            pupils           |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |           classes           |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |             opex            |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |           opexplan          |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |             hub             |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |             year            |     Schools\_Stats    |     -    |     -    |     -    |     +    |     +    |     -    |     -    |     -    |
    |            outid            |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |            birth            |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |         sextypename         |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |       classprofilename      |        Students       |     -    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |
    |         regtypename         |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |        classlangname        |        Students       |     -    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |
    |        KATOTTG\_2023        |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |        EDRPOU\_school       |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |             year            |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |            status           |        Students       |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |            outid            | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |             year            | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |           score100          | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |           score12           | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |
    |            score            | Students\_Take\_Tests |     -    |     -    |     +    |     +    |     +    |     +    |     +    |     +    |
    |         test\_status        | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |        test\_subject        | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |          test\_type         | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    | KATOTTG\_2023\_test\_center | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     +    |     +    |
    |     EDRPOU\_test\_center    | Students\_Take\_Tests |     +    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |
    |        KATOTTG\_2023        |      Test Centers     |     +    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |
    |             year            |      Test Centers     |     +    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |
    |            EDRPOU           |      Test Centers     |     +    |     +    |     +    |     +    |     +    |     +    |     -    |     -    |


- **Are relationships between individual instances made explicit (e.g., users' movie ratings, social network links)?** If so, please describe how these relationships are made explicit.

    Yes, they are explicit. To analyze relationships in the datasets, check the ER Diagram:

    ![](img/ER_diagram.png)


- **Are there recommended data splits (e.g., training, development/validation, testing)?** If so, please provide a description of these splits, explaining the rationale behind them.

    _We should come back when we decided which task we can do with this dataset_

- **Are there any errors, sources of noise, or redundancies in the dataset?** If so, please provide a description.

    The publicly available data from the Ukrainian Center for Educational Quality Assessment contains errors, so we cleaned and standardized it. The leading challenge with working with this open data over the years was a lack of standard data entry practices (sometimes even within the same year), the lack of a unified format of the data released year to year, and errors from manual data entry. Supplementary materials in the **associated paper** describe the whole cleaning process.

- **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?** If it links to or relies on external resources, a) are there guarantees that they will exist and remain constant over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.

    It was created based on an external resource – the [open data portal](https://zno.testportal.com.ua/opendata) of the Ukrainian Center for Educational Quality Assessment. We provide Jupyter notebooks and scripts to generate the datasets from the respective sources.

    1. This is guaranteed by the [law](https://ips.ligazakon.net/document/view/t112939?an=251&ed=2022_12_01) of Ukraine on access to public information. Information administrators are obliged to provide public information in the form of open data upon request, publish, and regularly update it on the unified state open data web portal and on their websites. These datasets are published via an open data portal.
    2. You can find the official archival versions of the datasets on the [open data portal](https://zno.testportal.com.ua/opendata). These datasets are depersonalized (so hidden some sensitive features) according to the Law of Ukraine "On Personal Data Protection."
    3. There are no restrictions for data usage, and the law of Ukraine guarantees it: “Public information in the form of open data is authorized for its further free use and distribution. Any person may freely copy, publish, distribute, use, including for commercial purposes, in combination with other information or by incorporating into their own product public information in the form of open data with a mandatory reference to the source of such information.”

    [Article 101](https://ips.ligazakon.net/document/view/t112939?an=251&ed=2022_12_01). Public information in the form of open data 

    The datasets about participants and their EIE or NMT results were published around August to September of the same year, starting in 2016. Annual education expenditure datasets are published around January-February of the following year, starting in 2018, but in 2022 publication was stopped due to the war in Ukraine.

- **Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** If so, please provide a description.

    Personal data in these datasets is depersonalized and protected in accordance with the Law of Ukraine ["On Personal Data Protection"](https://ips.ligazakon.net/document/view/t102297?an=0&ed=2022_10_27).

- **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** If so, please describe why.

    No.

- **Does the dataset relate to people?** If not, you may skip the remaining questions in this section.

    Yes, each instance in the Student and Students_take_tests datasets corresponds to a person.

- **Does the dataset identify any subpopulations (e.g., by age, gender)?** If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.

    Datasets identify subpopulations since each individual has features such as year of birth, gender, living location, type of school, etc.

- **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** If so, please describe how.

    To the best of our knowledge and according to the law of Ukraine, "On Personal Data Protection," it is impossible to identify individuals directly from the datasets. However, the possibility of reconstruction attacks combining data from the UCEQA and other data sources is a concern. Differential privacy

- **Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** If so, please provide a description.

    The datasets contain features such as a year of birth or gender that are often considered sensitive.

- **Any other comments?**

    No.

Collection process
------------------

- **How was the data associated with each instance acquired? Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)?** If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.

    The Ukrainian Center for Educational Quality Assessment (UCEQA) collected the data. The participant provided some information during registration (year of birth, gender, school, etc). The corresponding departments of UCEQA verified this data. According to the order of the Ministry of Education and Science of Ukraine: “The fact of receiving the registration card at the processing point is the basis for processing personal data in the process of preparing and conducting external independent evaluation, their use during admission to higher education institutions in accordance with the requirements of the Law of Ukraine "On Personal Data Protection." Information about the test centers and the results of EIE or NMT tests was added by UCEQA, as well as depersonalized data of all test participants. Results of EIE or NMT tests were obtained after the tests via defined evaluating systems. More details on the data are provided at [open data portal](https://zno.testportal.com.ua/opendata).

- **What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?** How were these mechanisms or procedures validated?

    The dataset contains the following:

    - Demographic data of test participants and their educational institutions were collected during registration. For EIE, data was provided by participants through the paper registration form and was used for manual human curation after. For NMT, data was provided by participants through the creation of a personal account on the website of the Ukrainian Center, entering personal data and information on participation in the ICT (Information and Communication System) of the UCEQA, and submission of the entered information and copies of documents to the regional center for processing.
    - EIE and NMT results, obtained from direct tests results (evaluating by machine in the case of EIE since it was paper-based and corresponding software in the case of NMT since it is computer-based), results of open (written) assignments in the case of EIE (evaluating by experts), corrected via the appeal process, and their conversion to various evaluating systems.
    - Information about test centers was created by UCEQA during the organizational procedure.

- **If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?**

    The dataset contains all possible instances of people who have registered for participation in EIE or NMT in the corresponding year. Some of the collected features (name, date of birth, etc) are hidden according to the law of Ukraine's “On Personal Data Protection".

- **Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?**

    The subjects of the EIE were the Ministry of Education and Science of Ukraine, the Ukrainian Center for Educational Quality Assessment, regional centers for educational quality assessment and the executive authority of the Autonomous Republic of Crimea in the field of education, structural units for education and science of regional, Kyiv and Sevastopol city state administrations. The data was collected by employees of all these organizations. We have no information on who was involved in the data collection process personally and how much they were paid.

    The subjects of the NMT were the Ministry of Education and Science of Ukraine, the Ukrainian Center for Educational Quality Assessment, regional centers for educational quality assessment, structural units for education and science of regional, Kyiv city state and military administrations, and higher education institutions. The data was collected through the ICT (Information and Communication System) of the UCEQA and the software where participants passed the test.

- **Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.

    Data was collected from 2016 to 2023 years. This timeframe matches the creation timeframe of the data associated with the instances.

- **Were any ethical review processes conducted (e.g., by an institutional review board)?** If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.

    As a government agency, the Ukrainian Center for Educational Quality Assessment is subject to government oversight mechanisms. For example, the testing process is in line with the provisions of the Convention for the Protection of Human Rights and Fundamental Freedoms and the case law of the European Court of Human Rights. Also, the process was approved by the All-Ukrainian Organization of Disabled People "Union of Organizations of Disabled People of Ukraine". Finally, The Ministry of Education and Science of Ukraine conducted an anti-discrimination examination.

- **Does the dataset relate to people?** If not, you may skip the remainder of the questions in this section.

    Yes.

- **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?**

    Data collection was performed by the Ukrainian Center for Educational Quality Assessment. We obtained the data from publicly available [Open Data resource](https://zno.testportal.com.ua/opendata).

- **Were the individuals in question notified about the data collection?** If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.

    Yes. It is written in the Order of the Ministry of Education and Science of Ukraine: “The fact of receiving the registration card at the processing point is the basis for processing personal data in the process of preparing and conducting external independent evaluation, their use during admission to higher education institutions in accordance with the requirements of the Law of Ukraine "On Personal Data Protection"” that publicly available on the website of Ukrainian Center for Educational Quality Assessment each year.

- **Did the individuals in question consent to the collection and use of their data?** If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.

    They consent by sending the registration documents to the Ukrainian Center for Educational Quality Assessment or by submitting the information through the Information and Communication System for the NMT.

- **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).

    No.

- **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?** If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.

    No.

- **Any other comments?**

    No.

Preprocessing/cleaning/labeling
-----------------------------------

- **Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** If so, please provide a description. If not, you may skip the remainder of the questions in this section.

    We used datasets from the open data portal of [the Ukrainian Center for Educational Quality Assessment](https://zno.testportal.com.ua/opendata). A leading challenge with working with this open data over the years is a lack of standard data entry practices (sometimes even within the same year) and the lack of a unified format of the data released year to year. In order to overcome this, we took several manual and automated data-cleaning steps. After that, the data was transformed into normalized tables and loaded into a PostgreSQL database. The main cleaning steps were connected with location data (that is highly inconsistent year over year, owing to the significant decommunization and decentralization that took place in Ukraine between 2016 and 2023), names of educational institutions (open data has many inconsistencies caused by renaming of the institutions several times and manual data entry).

    Supplementary materials in the **associated paper** describe the whole cleaning process.

- **Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?** If so, please provide a link or other access point to the "raw" data.

    The raw data from the Ukrainian Center for Educational Quality Assessment (UCEQA) can be found here: <https://zno.testportal.com.ua/opendata>. The raw data from the Ministry of Finance can be found here <https://mof.gov.ua/uk/the-reform-of-education>.

- **Is the software used to preprocess/clean/label the instances available? If so, please provide a link or other access point.**

    The code used to clean the data is all open source and available on the GitHub page <https://github.com/DataResponsibly/ZNO-Dataset>.

- **Any other comments?**

    No.

Uses
----

- **Has the dataset been used for any tasks already?** If so, please provide a description.

    ...

- **Is there a repository that links to any or all papers or systems that use the dataset?** If so, please provide a link or other access point.

    On the GitHub page, <https://github.com/DataResponsibly/ZNO-Dataset>, any public forks to the package are visible, and papers or systems that use the datasets should cite the paper linked to that GitHub page.

- **What (other) tasks could the dataset be used for?**

    New prediction tasks may be defined on the EIE data that use different subsets of variables as features and/or different target variables.

- **Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other undesirable harms (e.g., financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?

    The dataset is clean and complete. The user should know that every year, the minimum score for passing the exam for each subject is defined (please see the Appendix). So to compare two years according to one subject, the user should carefully investigate the content (we provide our suggestions on which years and subjects could be compared).

- **Are there tasks for which the dataset should not be used?** If so, please provide a description.

    This dataset contains personal information, and users should not attempt to re-identify individuals in it. Further, these datasets are meant primarily to aid in benchmarking machine learning algorithms. Substantive investigations into inequality, demographic shifts, and other important questions should not be based purely on the datasets we provide.

- **Any other comments?**

    No.

Distribution
------------

- **Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?** If so, please provide a description.

    The dataset will be available for public download on the GitHub page, <https://github.com/DataResponsibly/ZNO-Dataset>

- **How will the dataset will be distributed (e.g., tarball on website, API, GitHub)? Does the dataset have a digital object identifier (DOI)?**

    The dataset will be distributed via GitHub, see <https://github.com/DataResponsibly/ZNO-Dataset>. The dataset does not have a DOI.

- **When will the dataset be distributed?**

    The dataset will be released on January 1, 2025 and available thereafter for download and public use.

- **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.

    The EIE package and data loading code will be available under the MIT license. The EIE data itself is based on data from the Ukrainian Center for Educational Quality Assessment (UCEQA), public files managed by the UCEQA. For more information, see <https://zno.testportal.com.ua/opendata>. There are no restrictions for data usage, and it is guaranteed by the law of Ukraine “Public information in the form of open data is authorized for its further free use and distribution. Any person may freely copy, publish, distribute, use, including for commercial purposes, in combination with other information or by incorporating into their own product public information in the form of open data with a mandatory reference to the source of such information.” [Article 101.](https://ips.ligazakon.net/document/view/t112939?an=251&ed=2022_12_01) Public information in the form of open data 

- **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.

    No

- **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** If so, please describe these restrictions, and provide a link or other access point to or otherwise reproduce any supporting documentation.

    To our knowledge, no export controls or regulatory restrictions apply to the dataset.

- **Any other comments?**

    No.

Maintenance
-----------

- **Who is supporting/hosting/maintaining the dataset?**

    The dataset will be hosted on GitHub and supported and maintained by the NAME team. As of May 2023, this team consists of Nazarii Drushchak, Tetiana Zakharchenko, Olha Liuba, Oleksandra Konopatska, Andrew Bell, and Julia Stoyanovich.

- **How can the owner/curator/manager of the dataset be contacted (e.g., email address)?**

    Please send issues and requests to [ZNO_DATASET@gmail.com](ZNO_DATASET@gmail.com).

- **Is there an erratum?** If so, please provide a link or other access point.

    An erratum will be hosted on the dataset website, <https://github.com/DataResponsibly/ZNO-Dataset>.

- **Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?** If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?

    The dataset will be updated as required to address errors and refine the prediction problems based on feedback from the community. The package maintainers will update the dataset and communicate these updates on GitHub.

- **If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** If so, please describe these limits and explain how they will be enforced.

    The data used in ZNO_DATASET is based on data published by the Ukrainian Center for Educational Quality Assessment from publicly available open data resources, such as <https://zno.testportal.com.ua/opendata>. The data will be inherited, and the corresponding retention policies will be respected.

- **Will older versions of the dataset continue to be supported/hosted/maintained?** If so, please describe how. If not, please describe how its obsolescence will be communicated to users.

    Older versions of the datasets in ZNO_DATASET will be clearly indicated, supported, and maintained on the GitHub website. Each new version of the dataset will be tagged with version metadata and an associated GitHub release.

- **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.

    Users wishing to contribute to ZNO_DATASET are encouraged to do so by submitting a pull request on GitHub <https://github.com/DataResponsibly/ZNO-Dataset/pulls>. The contributions will be reviewed by the maintainers. These contributions will be reflected in the new version of the dataset and broadcasted as part of each Github release.

- **Any other comments?**

    No.