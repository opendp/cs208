# CS 208 (Applied Privacy for Data Science)

### Syllabus



Instructors: **[James Honaker](http://hona.kr/) and [Salil Vadhan](http://salil.seas.harvard.edu)**  

### Tentative Schedule

| **Date**             | **Title**     | **Slides/Notes** | **Advance Reading **(see also [annotated course bibliography](cs208_annotated_bibliography.pdf))
|----------------------|---------------|------------------ |---------------------------------------------------------------------------------------------------:|
| Mon 1/28 | Course overview |  [pdf](overview-slides.pdf) | |
| **Attacks on Privacy** |
| Fri 2/1 | Reidentification & reconstruction attacks: lecture | [pdf](reidentification and reconstruction-slides.pdf) | [Tanner](https://www.forbes.com/sites/adamtanner/2013/04/25/harvard-professor-re-identifies-anonymous-volunteers-in-dna-study/#4b8a122d92c9), [Barbaro-Zeller](https://www.nytimes.com/2006/08/09/technology/09aol.html), [Narayanan-Shmatikov](https://dl.acm.org/citation.cfm?id=1743558) |
| Mon 2/4 | Reidentification & reconstruction attacks: practicum | [pdf](reconstruction-practicum.pdf) | [Cohen-Nissim](https://arxiv.org/abs/1810.05692),[Garfinkel-Abowd-Martindale](https://dl.acm.org/citation.cfm?id=3295691) |
| Fri 2/8 | Membership attacks & other attacks: lecture | [pdf](membership-lecture.pdf) | [Shokri slides](https://www.dropbox.com/s/hfz1rdf6eu31snj/01-Reza Shokri-Membership Inference Attacks against Machine Learning Models.pdf) | [P3G Consortium et al.](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000665),  [Korolova (§1,4,6,8)](https://journalprivacyconfidentiality.org/index.php/jpc/article/view/594) |
| Mon 2/11 | Membership attacks & other attacks: practicum | [pdf](membership-practicum.pdf) | none |
| Problem Set 1 (due Tue 2/26) | | [pdf](ps1.pdf) | |
| **Foundations of Differential Privacy** |
| Fri 2/15 | Definition, basic mechanisms: lecture | [pdf](DP-foundations1-lecture.pdf) | [DP Primer (§ III-IV.C)](http://www.jetlaw.org/journal-archives/volume-21/volume-21-issue-1/differential-privacy-a-primer-for-a-non-technical-audience/) |
| Mon 2/18 | No class: President's Day | |
| Fri 2/22 | Definition, basic mechanisms: practicum | [pdf](DP-foundations1-practicum.pdf) | [Dwork-Roth (Ch.3 only pages 28-33 § 3.1-Example 3.2 in §3.3)](https://www.nowpublishers.com/article/Details/TCS-042) |
| Mon 2/25 | Properties, more mechanisms: lecture | [pdf](DP-foundations2-lecture.pdf) | [DP Primer (§ IV.D-VI.B)](http://www.jetlaw.org/journal-archives/volume-21/volume-21-issue-1/differential-privacy-a-primer-for-a-non-technical-audience/) |
| Fri 3/1 | Properties, more mechanisms: practicum | [pdf](DP-foundations2-practicum.pdf) | none |
| Problem Set 2 (due Tue 3/12) | | [pdf](ps2.pdf) |  |
| **Implementing (Centralized) Differential Privacy** |
| Mon 3/4 | One-shot releases (histograms, synthetic data, Census): lecture | [pdf](oneshot-lecture.pdf) | [Garfinkel-Abowd-Powazek](https://dl.acm.org/citation.cfm?id=3268949)[Gaboardi-Arias-Hsu-Roth-Wu (§1,7,8)](https://journalprivacyconfidentiality.org/index.php/jpc/article/view/650) | 
| Fri 3/8 | One-shot releases: practicum | [pdf](oneshot-practicum.pdf) | [Chetty-Friedman-Hendren-Jones-Porter-A](https://opportunityinsights.org/wp-content/uploads/2018/10/atlas_summary.pdf), [Chetty-Friedman-Hendren-Jones-Porter-B (§III)](https://opportunityinsights.org/wp-content/uploads/2018/10/atlas_paper.pdf) |
| Mon 3/11 | Query/programming interfaces: lecture | [pdf](programming-lecture.pdf) | none |
| Fri 3/15 | Query/programming interfaces: practicum | [pdf](programming-practicum.pdf) | [Gaboardi-Honaker-King-Murtagh-Nissim-Ullman-Vadhan](https://arxiv.org/abs/1609.04340) |
| Problem Set 3 (due Tue 4/2) | | [pdf](ps3.pdf) | | 
| Mon 3/18 | No class: Spring Break | |
| Fri 3/22 | No class: Spring Break | |
| **Local Differential Privacy** |
| Mon 3/25 | Foundations of Local DP: lecture | [pdf](localDP-foundations-lecture.pdf) | none |
| Fri 3/29 | Foundations of Local DP: practicum | [pdf](localDP-foundations-practicum.pdf) | none |
| Mon 4/1 | Implementing Local DP (Google, Apple, Microsoft): lecture | [pdf](localDP-implementations-lecture.pdf) | [Apple's Learning with Privacy at Scale](https://machinelearning.apple.com/2017/12/06/learning-with-privacy-at-scale.html) |
| Fri 4/5 | Implementing Local DP: practicum | [pdf](localDP-implementations-practicum.pdf) | none |
| Problem Set 4a (due Tue 4/16) | | [pdf](ps4a.pdf) | |
| **Additional Topics** |
| Mon 4/8 | Machine Learning with DP: lecture | [pdf](MLwithDP-lecture.pdf) | none |
| Fri 4/12 | Machine Learning with DP: practicum | [pdf](MLwithDP-practicum.pdf) | [Radebaugh-Erlingsson](https://medium.com/tensorflow/introducing-tensorflow-privacy-learning-with-differential-privacy-for-training-data-b143c5e801b6) |
| Mon 4/15 | DP for graphs & social networks | [pdf](graphprivacy-lecture.pdf) | none |
| Problem Set 4b (due Tue 4/30) | | [pdf](ps4b.pdf) |  |
| Fri 4/19 | Law & policy I | none | [Solove "A Taxonomy of Privacy" (Introduction and §B, C1-4.)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=667622), [Nissim-Bembenek-Wood-Bun-Gaboardi-Gasser-O’Brien-Steinke-Vadhan (§IIC)](https://privacytools.seas.harvard.edu/files/02.-article-wood-7.21.pdf) |
| Mon 4/22 | Law & policy II (guest: [Alexandra Wood](https://cyber.harvard.edu/people/awood)) | [pdf](Bridging the Gap between Computer Science and Legal Approaches to Privacy (CS208).pdf) | [Nissim-Bembenek-Wood-Bun-Gaboardi-Gasser-O’Brien-Steinke-Vadhan (§IIIB, IIIC, IVA, IVB)](https://privacytools.seas.harvard.edu/files/02.-article-wood-7.21.pdf) |
| Fri 4/26 | Industry & government panel (guests Philip LeClerc, I[lya Mironov](https://ai.google/research/people/IlyaMironov), and [Ryan Rogers](https://www.math.upenn.edu/~ryrogers/)) | |
| Mon 4/29 | Conclusions | [pdf](conclusions.pdf) |
| **Final Project Deadlines (no late days)** | | [project guidelines](project-guidelines.pdf) | |
| Fri 5/10 | Draft of final papers due | |
| Mon 5/13-Tue 5/14 | Project presentations | |
| Fri 5/17 | Revised final papers due | |
