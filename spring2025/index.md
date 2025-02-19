# CS 2080 (Applied Privacy for Data Science)

**Instructors**: Salil Vadhan, James Honaker, and Priyanka Nanayakkara

**Teaching Fellows**: Zachary Ratliff, Christian Aagnes, Sahil Kuchlous, Jason Tang, and Yanis Vandecasteele

**Regular meeting time**: Mondays & Wednesdays 11:15-12:30, starting 1/25

**Location**: 2.112 in 114 Western Ave, Allston, MA (in the building next to the SEC)

### Resources
* [Syllabus](files/syllabus.pdf)
* [Discussions on Ed](https://edstem.org/us/courses/74326)
* [Reading on Perusall](https://app.perusall.com/courses/compsci-2080-applied-privacy-for-data-science/)[ (reading & commenting guidelines)](https://opendp.github.io/cs208/spring2025/files/reading_and_commenting_guidelines.pdf)
* [Annotated Course Bibliography]( https://opendp.github.io/cs208/spring2025/files/cs208_annotated_bibliography.pdf)
* [Course Google Calendar](https://calendar.google.com/calendar/u/0?cid=Y19jMDljODBmYmE0ZjdiMjg1YWRmMDU1NzgyYjM2NDAxODZjZWVmYzliZTM4Yzk5YzZjMzU5Yjg0ZTBmZjI4MWVlQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20)
* Video Recordings at Panopto (access via Canvas)

### Schedule

| Date                                     | Title                                          | Slides/Notes                                                    | Advance Reading                                                                                                 |
|------------------------------------------|------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Monday (1/27)                            | Course Overview                                | [pdf](lectures/lecture-1-overview.pdf)                                                  |                                                                                                                 |
| **Attacks on Privacy**                     |                                                |                                                                 |
| Wednesday (1/29)                         | Re-identification Attacks                      | [pdf](lectures/lecture-2-reidentification-reconstruction-attacks.pdf)                                                                | Hands-On Differential Privacy, Chapter 11  |
| Problem Set 1 (due Fri 2/7)              |                                                | [pdf](homeworks/ps1/ps1.pdf), [tex](homeworks/ps1/ps1.tex)                |                  |
| Monday (2/3)                             | Reconstruction Attacks                         | [pdf1](lectures/lecture-3-discussion-and-reconstruction-attacks-practicum.pdf), [ipynb](examples/wk2_regression_attack.ipynb), [pdf2](lectures/lecture-3-part-2.pdf)  | [Tanner], [Narayanan-Shmatikov], [Castro-Cavoukian]
| Wednesday (2/5)                          | Membership Inference Attacks                   | [pdf](lectures/lecture-4-membership-attacks.pdf)                 | [Ruggles-van Riper], [Jessica Hullman blog post], [Smith-Ullman]                                                            |
| Problem Set 2 (due Fri 2/14)              |                                                | [pdf](homeworks/ps2/ps2.pdf), [tex](homeworks/ps2/ps2.tex)                |                  |
| **DP Foundations**                       |                                               |                                                                  |                                         |
| Monday (2/10)                            | DP Foundations: Definitions, Basic Mechanisms  |  [pdf1](lectures/lecture-4b-membership-attack-review.pdf), [ipynb class example](examples/wk2b_membership_attack.ipynb), [ipynb w/ in-class updates](examples/wk2b_membership_attack_fixed.ipynb), [pdf2](lectures/lecture-5-dp-foundations.pdf)                 |  [P3G Consortium et al.], Hands-On Differential Privacy, Chapter 2 (up to pg. 35)                               |
| Wednesday (2/12)                         | DP Foundations: Properties of DP Mechanisms    |  [pdf](lectures/lecture-6-dp-foundations-p2.pdf), [ipynb class example](examples/wk3_laplace_mechanism.ipynb)                                                            | Hands-on Differential Privacy Ch. 2, pg 35-52                                     |
| Monday (2/17) **No Class** - President's Day               |                               |                                                               |                                     |
| Wednesday (2/19)                         | Composition                                     | [pdf](lectures/lecture-7-composition.pdf)                     | Hands-On Differential Privacy, Ch. 3      |

[Tanner]: https://www.forbes.com/sites/adamtanner/2013/04/25/harvard-professor-re-identifies-anonymous-volunteers-in-dna-study/#4b8a122d92c9
[Barbaro-Zeller]: https://www.nytimes.com/2006/08/09/technology/09aol.html
[Narayanan-Shmatikov]: https://dl.acm.org/citation.cfm?id=1743558
[Castro-Cavoukian]: https://www2.itif.org/2014-big-data-deidentification.pdf
[Smith-Ullman]: https://dpcourse.github.io/2023-spring/lecnotes-web/dpcourse-S21-lec-02-03-reconstruction.pdf
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
[Nissim-Wood]: https://privacytools.seas.harvard.edu/files/privacytools/files/nissim_wood_-_is_privacy_privacy_.pdf
[Cohen]: https://cdn.harvardlawreview.org/wp-content/uploads/pdfs/vol126_cohen.pdf
[Solove]: https://deliverypdf.ssrn.com/delivery.php?ID=785068073073025084118014104076101007098032068060033065078102095014099121031107087031057121038126047045032106114097020094095108035045012081119009013007028118119077041022082071125065>[Sarathy]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4079222
[Winner]: https://faculty.cc.gatech.edu/~beki/cs4001/Winner.pdf
[Green-Viljoen]: https://www.benzevgreen.com/20-fat-realism/
[Mulligan-Koopman-Doty]: https://www.law.berkeley.edu/wp-content/uploads/2017/07/Privacy-is-an-essentially.pdf
