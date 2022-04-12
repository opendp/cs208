# CS 208 (Applied Privacy for Data Science)

**Instructors**: Salil Vadhan, James Honaker, and Wanrong Zhang

**Teaching Fellows**: Daniel Alabi, Jayshree Sarathy, Michael Shoemate, and Connor Wagaman

**Regular meeting time**: Tuesdays & Thursdays 11:15-12:30, starting 1/25

**Location**: Harvard Science & Engineering Complex SEC LL2.221, 150 Western Ave, Allston, MA

### Resources

* [Syllabus]
* [Google Calendar link][gcal]
* [Discussions at ed][ed]
* [Reading at Perusall][perusall] ([reading guidelines])
* Video recordings at Panopto (access via Canvas)
* [Annotated Course Bibliography]
* [Guidelines for Reading and Commenting]
* [Example Notebooks (GitHub)]
* [Final project guidelines]

[Syllabus]: https://opendp.github.io/cs208/spring2022/files/cs208_spring2022_syllabus.pdf
[gcal]: https://calendar.google.com/calendar/u/0?cid=Y19lYjYwZ2NzcDdoZTBwamZqMG1ldGs0NnE3MEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t
[ed]: https://edstem.org/us/courses/19868/
[perusall]: https://app.perusall.com/courses/compsci-208-applied-privacy-for-data-science/
[reading guidelines]: files/reading_and_commenting_guidelines.pdf
[Annotated Course Bibliography]: files/cs208_annotated_bibliography.pdf
[Guidelines for Reading and Commenting]: https://opendp.github.io/cs208/spring2022/files/reading_and_commenting_guidelines.pdf
[Example Notebooks (GitHub)]: https://github.com/opendp/cs208/tree/main/spring2022/examples
[Final project guidelines]: https://github.com/opendp/cs208/tree/main/spring2022/final%20project/Final%20Project%20Guidelines.pdf


### Schedule

| Date                                     | Title                                          | Slides/Notes                                                    | Advance Reading                                                                                                 |
|------------------------------------------|------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Tue 1/18                                 | Course Preview                                 | [pdf][jan18:pdf], [Recording][jan18:video]                      |                                                                                                                 |
| **Attacks on Privacy**                   |                                                |                                                                 |                                                                                                                  |
| Tue 1/25                                 | Course Overview & Attacks on Privacy           | [pdf][jan25:pdf]                                                |                                                                                                                 |
| Thu 1/27                                 | Reconstruction Attacks                         | [pdf](presentations/reconstruction.pdf)                         | [Tanner], [Barbaro-Zeller], [Narayanan-Shmatikov]                                                               |
| Problem Set 1 (due Weds 2/2)             |                                                | [pdf](homework/hw1.pdf), [tex](homework/hw1.tex)                |                                                                                                                 |
| Section 1                                |                                                | [pdf](section/section1.pdf)                                     |                                                                                                                 |
| Tue 2/01                                 | Reconstruction & Membership Attacks            | [pdf](presentations/membership.pdf)                             | [Smith-Ullman] Reconstruction lecture notes (Sec 1-2.1, Sec 3), [Ruggles-van Riper], [Jessica Hullman blog post] |
| Thu 2/03                                 | Membership Attacks                             | [pdf](presentations/membership-attacks.pdf), [ipynb][wk2_mem]   | [P3G Consortium et al.],  [Korolova (§1,4,6,8)]                                                                 |
| Problem Set 2 (due Fri 2/11)             |                                                | [pdf](homework/hw2.pdf), [tex](homework/hw2.tex)                |                                                                                                                  |
| Section 2                                |                                                | [pdf](section/section2.pdf)                                     |                                                                                                                 |
| **Foundations of Differential Privacy**  |                                                |                                                                 |                                                                                                                 |
| Tue 2/08                                 | Definition, basic mechanisms                   | [pdf](presentations/DP-foundations1.pdf)                        | [DP Primer Secs III-IV.B]                                                                                       |
| Thu 2/10                                 | DP Foundations: the Laplace Mechanism          | [pdf](presentations/DP-laplace.pdf), [ipynb][wk3_lap]           | [U.S. Broadband Coverage Data Set](https://arxiv.org/pdf/2103.14035v2.pdf), [Smith-Ullman] Lecture 4 (Sec 4)     |
| Problem Set 3 (due Fri 2/18)             |                                                | [pdf](homework/hw3.pdf), [tex](homework/hw3.tex)                |                                                                                                                 |
| Section 3                                |                                                | [pdf](section/section3.pdf)                                     |                                                                                                                 |
| Tue 2/15                                 | More DP Foundations                            | [pdf](presentations/DP-foundations2.pdf)                        | [DP Primer Secs IV.C-VI.B]                                                                                      |
| Thu 2/17                                 | The Gaussian Mechanism                         | [pdf](presentations/DP-gaussian-mechanism.pdf), [ipynb wk4_*]   | [Smith-Ullman] Lecture 5 (Sec 1), Lecture 9 (Lemma 1.2, Sec 2 up to Thm 2.1), Lecture 10 (Sec 1)        |
| Problem Set 4 (due Fri 2/25)             |                                                | [pdf](homework/hw4.pdf), [tex](homework/hw4.tex)                |
| Section 4                                |                                                | [pdf](section/section4.pdf)                                     |  
| Tue 2/22                                 | Beyond Noise Addition                          | [pdf](presentations/beyond-noise.pdf), [ipynb][wk5_exponential] | [Smith-Ullman] Lecture 6 (Secs 1.0-1.1), [Smith-Raskhodnikova encyclopedia] article: DP for graph data            |
| **Implementing Centralized DP** |                                       |                                                                 |      
| Thu 2/24                                 | Synthetic Data: the 2020 Census                | [pdf](presentations/DP_CensusSynthetic.pdf)                     | [2020 Census Data Products and Privacy Methods] (Secs 2.0-2.2, 3, 5.0)                               |
| Problem Set 5 (due Fri 3/4)              |                                                | [pdf](homework/hw5.pdf), [tex](homework/hw5.tex)                |
| Section 5                                |                                                | [pdf](section/section5.pdf)                                     |  
| Tue 3/1                                  | Statistical Releases: the Opportunity Atlas    | [pdf](presentations/DP_CensusSynthetic.pdf)                           | [Opportunity Atlas]; [Chetty-Friedman JPC] (Sec 3)                                                                |
| Tue 3/1 and Thu 3/3                      | Machine Learning with DP                       | [pdf](presentations/DP_OI_SGD.pdf), [ipynb](examples/wk6_dpsgd_full.ipynb)                              | [Deep Learning with DP] (Secs 1-3.1, 5.2)                                                               |
| Problem Set 6 (due Fri 3/11)             |                                                | [pdf](homework/hw6.pdf), [tex](homework/hw6.tex)                |
| Section 6                                |                                                | [pdf](section/section6.pdf)                                     | 
| Tue 3/8                                  | Machine Learning with DP (cont'd)              | [pdf](presentations/MLwithDP-lecture.pdf), [ipynb](examples/wk7_opacus_example.ipynb)                       |   |
| Thu 3/10                                 | Embedded EthiCS module                         |  [pdf](presentations/Embedded-EthiCS-module.pdf)                | Nissenbuam, Privacy in Context (Intro and Ch 7)                                                   |
| Problem Set 7 (due Fri 3/25)             |                                                | [pdf](homework/hw7.pdf), [tex](homework/hw7.tex)                |
| Embedded EthiCS Assignment (due Fri 3/25)|                                                | [pdf](homework/hw7_Embedded_EthiCS.pdf)              |
| Section 7                                |                                                | [pdf](section/section7.pdf)                                     | 
| Tue 3/22                                 | Programming Frameworks and Query Systems       |  [pdf](presentations/programming-query.pdf)                                                                |  [DP for DB] (Secs 7.0, 7.2, 7.3, 7.6, 8.0, 8.1)                                                          |
| Thu 3/24                                 | OpenDP       |  [pdf](presentations/programming-query-2.pdf), [ipynb][wk8_opendp]                                                               |  [PSI] (Secs 0-3)            |
| Problem Set 8a (due Fri 4/1)             |                                                | [pdf](homework/hw8.pdf), [tex](homework/hw8.tex)                |
| Section 8                                |                                                | [ipynb](section/section8.ipynb)                                 | 
| **Local and Distributed Models**         |                                       |                                                                 |      
| Tue 3/29                                 | Local Model: Foundations                       | [pdf](presentations/localDP-foundations-lecture.pdf)                                                               |              |
| Thu 3/31                                 | Local Model: Practicum                         | [pdf](presentations/localDP-practicum.pdf)            |     [Learning with Privacy at Scale]         |
| Section 9                                |                                                | [pdf](section/section9.pdf)                                 | 
| Tue 4/05                                 | Local Model: Implementations                   | [pdf](presentations/localDP-implementations.pdf)            |     [Federated Learning and Privacy]         |
| Thurs 4/07                               | Other Distributed Models: Foundations          | [pdf](presentations/distributedmodels.pdf)            |       [DP for DB] (Chapter 9)         |
| Problem Set 8b (due Fri 4/15)            |                                                | [pdf](homework/hw8b.pdf)               |
| Section 10                               |                                                |                                 | 
| Tues 4/12                                | Other Distributed Models: Implementations      | [pdf](presentations/end-to-end-privacy.pdf)           |   [Privacy-Preserving RCT]           |
| **Societal Perspectives on Privacy**     |                                       |                                                                 |     
| Thurs 4/14                               | Perspectives on Privacy: Law and Policy                  |             |              |
| Section 11                               |                                                |                                 | 
| Tues 4/19                                | Perspectives on Privacy: Science & Technology Studies                 |             |              |
| Thurs 4/21                               | Industry and Government Panel                  |             |              |
| Tues 4/26                                | Conclusions                 |             |              |
| Mon-Tues 5/9-10                          | Project Presentations                 |             |              |

[jan18:pdf]: files/course_preview.pdf
[jan18:video]: https://harvard.zoom.us/rec/play/rNU5_swSdM3xVtAd3rTReJtniCNhE4oKY54CWsA2hIPpnt2PmZGPbO-yOvIs0NpIS9y1ilRJ6SWsvH9P.hVnF5j1z4LYMDVYM

[jan25:pdf]: presentations/overview-reidentification.pdf
[wk2_mem]: examples/wk2_membership_attack.ipynb
[wk3_lap]: examples/wk3_laplace_mechanism_and_opendp.ipynb
[ipynb wk4_*]: https://github.com/opendp/cs208/tree/main/spring2022/examples
[wk5_exponential]: examples/wk5_exponential.ipynb

[Tanner]: https://www.forbes.com/sites/adamtanner/2013/04/25/harvard-professor-re-identifies-anonymous-volunteers-in-dna-study/#4b8a122d92c9
[Barbaro-Zeller]: https://www.nytimes.com/2006/08/09/technology/09aol.html
[Narayanan-Shmatikov]: https://dl.acm.org/citation.cfm?id=1743558
[Smith-Ullman]: https://dpcourse.github.io/
[Smith-Raskhodnikova encyclopedia]: https://link.springer.com/referenceworkentry/10.1007/978-3-642-27848-8_549-1
[Ruggles-van Riper]: https://link.springer.com/article/10.1007%2Fs11113-021-09674-3
[Jessica Hullman blog post]: https://statmodeling.stat.columbia.edu/2021/08/27/shots-taken-shots-returned-regarding-the-census-motivation-for-using-differential-privacy-and-btw-its-not-an-algorithm
[P3G Consortium et al.]: https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000665
[Korolova (§1,4,6,8)]: https://journalprivacyconfidentiality.org/index.php/jpc/article/view/594
[DP Primer Secs III-IV.B]: https://salil.seas.harvard.edu/files/salil/files/differential_privacy_primer_nontechnical_audience.pdf
[DP Primer Secs IV.C-VI.B]: https://salil.seas.harvard.edu/files/salil/files/differential_privacy_primer_nontechnical_audience.pdf
[2020 Census Data Products and Privacy Methods]: https://www2.census.gov/programs-surveys/decennial/2020/program-management/planning-docs/2020-census-data-products-privacy-methods.pdf
[Chetty-Friedman JPC]: https://journalprivacyconfidentiality.org/index.php/jpc/article/view/716/688
[Opportunity Atlas]: https://opportunityinsights.org/wp-content/uploads/2018/10/atlas_summary.pdf
[Deep Learning with DP]: https://arxiv.org/abs/1607.00133
[DP for DB]: https://dpfordb.github.io/
[PSI]: https://privacytools.seas.harvard.edu/publications/psipaper
[wk8_opendp]: examples/wk8_opendp.ipynb
[Learning with Privacy at Scale]: https://docs-assets.developer.apple.com/ml-research/papers/learning-with-privacy-at-scale.pdf
[Federated Learning and Privacy]: https://cacm.acm.org/magazines/2022/4/259417-federated-learning-and-privacy/fulltext
[Privacy-Preserving RCT]: https://dl.acm.org/doi/10.1145/3474123.3486764
