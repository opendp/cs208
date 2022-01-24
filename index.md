# CS 208 (Applied Privacy for Data Science)

### Overview

Data scientists, including industry analysts, scientific researchers and data-driven policy makers,
often want to analyze data that contains sensitive personal information that must remain private.
However, common techniques for data sharing that attempt to preserve privacy either bring
great privacy risks or great loss of information. Moreover, the increasing ability of big data,
ubiquitous sensors, and social media to record lives in detail brings new ethical responsibilities
to safeguard privacy.
The traditional approach to protecting privacy when sharing data is to remove "personally
identifying information,'' but it is now known that this approach does not work, because
seemingly innocuous information is often sufficient to uniquely identify individuals. A long
literature has shown that anonymization techniques for data releases are generally open to
reidentification attacks. Indeed, there have been many high-profile examples in which
individuals in supposedly anonymized datasets were re-identified by linking the remaining fields
with other, publicly available datasets. Aggregated information can reduce but not prevent this
risk, while also reducing the utility of the data to researchers.
This class will provide an overview of the risks of private data leakage in data science
applications and a firm foundation in how to measure and protect against these risks using the
framework of differential privacy, together with a hands-on examination of how to build
algorithms and software to preserve privacy, including a review of the deployed solutions in
industry and government.
Differential privacy, deriving from roots in cryptography, is a formal, mathematical conception of
privacy preservation. It guarantees that any released statistical result does not reveal
information about any single individual. That is, the distribution of answers one would get with
differentially private algorithms from a dataset that does not include myself must be
indistinguishable from the distribution of answers where I have added my own information.
Using differential privacy enables us to provide wide access to statistical information from a
privacy sensitive dataset without worries of individual-level information being leaked
inadvertently or due to an adversarial attack. There is now both a rich theoretical literature on
differential privacy and numerous efforts to bring differential privacy closer to practice, including
large-scale deployments by Google, Apple, Microsoft and the US Census Bureau. This course
will set out a foundation in the underlying theory of differential privacy, and then consider the
practical elements of implementing and deploying privacy-preserving techniques for data
analysis.


## Spring 2022



