# CS 208 (Applied Privacy for Data Science)

**Instructors**: Salil Vadhan, James Honaker, and Wanrong Zhang

**Teaching Fellows**: Daniel Alabi, Jayshree Sarathy, Michael Shoemate, and Connor Wagaman

**Regular meeting time**: Tuesdays & Thursdays 11:15-12:30, starting 1/25

**Location**: Harvard Science & Engineering Complex SEC LL2.221, 150 Western Ave, Allston, MA

If you have not done so already, please fill out the [background survey](https://docs.google.com/forms/d/e/1FAIpQLSfYrvV08oMJr5idotBG1eIyE6rafbKymxs_8gm9iUqpC73vKg/viewform).

Access the (updated) syllabus [here](files/cs208_spring2022_syllabus.pdf).


### Resources

* [Discussions at ed][ed]
* [Reading at Perusall][perusall] ([reading guidelines])
* Video recordings at Panopto (access via Canvas)
 
[ed]: https://edstem.org/us/courses/19868/
[perusall]: https://app.perusall.com/courses/compsci-208-applied-privacy-for-data-science/
[reading guidelines]: files/reading_and_commenting_guidelines.pdf


### Schedule

* [Google Calendar link][gcal]

[gcal]: https://calendar.google.com/calendar/u/0?cid=Y19lYjYwZ2NzcDdoZTBwamZqMG1ldGs0NnE3MEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t


| **Date**                                 | **Title**                            | **Slides/Notes/Videos**                          |          **Advance Reading** (see also [annotated course bibliography]) 
|------------------------------------------|-------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------:|
| Tue 1/18                                 | Course Preview                       | [pdf][jan18:pdf], [Recording][jan18:video]       |                                                                                                                 |
| **Attacks on Privacy**                   |
| Tue 1/25                                 | Course Overview & Attacks on Privacy | [pdf][jan25:pdf]                                 |                                                                                                                 |
| Thu 1/27                                 | Reconstruction Attacks               | [pdf](presentations/reconstruction.pdf)          |                                                               [Tanner], [Barbaro-Zeller], [Narayanan-Shmatikov] |
| Problem Set 1 (due Weds 2/2)             |                                      | [pdf](homework/hw1.pdf), [tex](homework/hw1.tex) |                                                                                                                 |
| Section 1                                |                                      | [pdf](section/section1.pdf)                      |                                                                                                                 |
| Tue 2/01                                 | Reconstruction & Membership Attacks  | [pdf](presentations/membership.pdf)              | [Smith-Ullman] Reconstruction lecture notes, Sec 1-2.1, Sec 3, [Ruggles-van Riper], [Jessica Hullman blog post] |
| Thu 2/03                                 | Membership Attacks                   | [pdf](presentations/membership-attacks.pdf)      |                                                                 [P3G Consortium et al.],  [Korolova (§1,4,6,8)] |
| Problem Set 2 (due Fri 2/11)             |                                      | [pdf](homework/hw2.pdf)                          |    
| Section 2                                |                                      | [pdf](section/section2.pdf)                      | 
| **Foundations of Differential Privacy**  |
| Tue 2/08                                 | Definition, basic mechanisms         | [pdf](presentations/DP-foundations1.pdf)         |                                                                                       [DP Primer Secs III-IV.B] |
| Thu 2/10                                 | DP Foundations: the Laplace Mechanism| [pdf](presentations/DP-laplace.pdf)              |                                                                                       [U.S. Broadband Coverage Data Set: A Differentially Private Data Release](https://arxiv.org/pdf/2103.14035v2.pdf), [Smith-Ullman] Lecture 4, Sec 4  |
| Problem Set 3 (due Fri 2/18)             |                                      | [pdf](homework/hw3.pdf)                          |
| Section 3                                |                                      | [pdf](section/section3.pdf)                      | |
| Tue 2/15                                 | More DP Foundations                  | [pdf](presentations/DP-foundations2.pdf)         |                                                                                       [DP Primer Secs IV.C-VI.B] |
| Thu 2/17                                 | The Gaussian Mechanism               | [pdf](presentations/DP-gaussian-mechanism.pdf)   |                                                                                       [Smith-Ullman] Lecture 5 Sec 1, Lecture 9 (Lemma 1.2), Lecture 9, Sec 2 up to Thm 2.1, Lecture 10 Sec 1. |
| Problem Set 4 (due Fri 2/25)             |                                      | [pdf](homework/hw4.pdf)                          |

[jan18:pdf]: files/course_preview.pdf
[jan18:video]: https://harvard.zoom.us/rec/play/rNU5_swSdM3xVtAd3rTReJtniCNhE4oKY54CWsA2hIPpnt2PmZGPbO-yOvIs0NpIS9y1ilRJ6SWsvH9P.hVnF5j1z4LYMDVYM

[jan25:pdf]: presentations/overview-reidentification.pdf

[annotated course bibliography]: files/cs208_annotated_bibliography.pdf
[Tanner]: https://www.forbes.com/sites/adamtanner/2013/04/25/harvard-professor-re-identifies-anonymous-volunteers-in-dna-study/#4b8a122d92c9
[Barbaro-Zeller]: https://www.nytimes.com/2006/08/09/technology/09aol.html
[Narayanan-Shmatikov]: https://dl.acm.org/citation.cfm?id=1743558
[Smith-Ullman]: https://dpcourse.github.io/
[Ruggles-van Riper]: https://link.springer.com/article/10.1007%2Fs11113-021-09674-3
[Jessica Hullman blog post]: https://statmodeling.stat.columbia.edu/2021/08/27/shots-taken-shots-returned-regarding-the-census-motivation-for-using-differential-privacy-and-btw-its-not-an-algorithm
[P3G Consortium et al.]: https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000665
[Korolova (§1,4,6,8)]: https://journalprivacyconfidentiality.org/index.php/jpc/article/view/594
[DP Primer Secs III-IV.B]: https://salil.seas.harvard.edu/files/salil/files/differential_privacy_primer_nontechnical_audience.pdf
[DP Primer Secs IV.C-VI.B]: https://salil.seas.harvard.edu/files/salil/files/differential_privacy_primer_nontechnical_audience.pdf
