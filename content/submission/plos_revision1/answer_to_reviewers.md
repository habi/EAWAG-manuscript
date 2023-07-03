
PONE-D-23-10896
Microtomographic investigation of a large corpus of cichlids
PLOS ONE

Dear Dr. Haberthür,

Thank you for submitting your manuscript to PLOS ONE. After careful consideration, we feel that it has merit but does not fully meet PLOS ONE’s publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript by Aug 14 2023 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at plosone@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pone/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

    A rebuttal letter that responds to each point raised by the academic editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'.
    A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.
    An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, please include your updated statement in your cover letter. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

If applicable, we recommend that you deposit your laboratory protocols in protocols.io to enhance the reproducibility of your results. Protocols.io assigns your protocol its own identifier (DOI) so that it can be cited independently in the future. For instructions see: https://journals.plos.org/plosone/s/submission-guidelines#loc-laboratory-protocols. Additionally, PLOS ONE offers an option for publishing peer-reviewed Lab Protocol articles, which describe protocols hosted on protocols.io. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols.

We look forward to receiving your revised manuscript.

Kind regards,

[REDACTED]





Journal requirements:

When submitting your revision, we need you to address these additional requirements.

1. Please ensure that your manuscript meets PLOS ONE's style requirements, including those for file naming. The PLOS ONE style templates can be found at

https://journals.plos.org/plosone/s/file?id=wjVg/PLOSOne_formatting_sample_main_body.pdf and

https://journals.plos.org/plosone/s/file?id=ba62/PLOSOne_formatting_sample_title_authors_affiliations.pdf

2. In your Data Availability statement, you have not specified where the minimal data set underlying the results described in your manuscript can be found. PLOS defines a study's minimal data set as the underlying data used to reach the conclusions drawn in the manuscript and any additional data required to replicate the reported study findings in their entirety. All PLOS journals require that the minimal data set be made fully available. For more information about our data policy, please see http://journals.plos.org/plosone/s/data-availability.

Upon re-submitting your revised manuscript, please upload your study’s minimal underlying data set as either Supporting Information files or to a stable, public repository and include the relevant URLs, DOIs, or accession numbers within your revised cover letter. For a list of acceptable repositories, please see http://journals.plos.org/plosone/s/data-availability#loc-recommended-repositories. Any potentially identifying patient information must be fully anonymized.

Important: If there are ethical or legal restrictions to sharing your data publicly, please explain these restrictions in detail. Please see our guidelines for more information on what we consider unacceptable restrictions to publicly sharing data: http://journals.plos.org/plosone/s/data-availability#loc-unacceptable-data-access-restrictions. Note that it is not acceptable for the authors to be the sole named individuals responsible for ensuring data access.

We will update your Data Availability statement to reflect the information you provide in your cover letter.






[Note: HTML markup is below. Please do not edit.]

Reviewers' comments:

Reviewer's Responses to Questions

Comments to the Author

1. Is the manuscript technically sound, and do the data support the conclusions?

The manuscript must describe a technically sound piece of scientific research with data that supports the conclusions. Experiments must have been conducted rigorously, with appropriate controls, replication, and sample sizes. The conclusions must be drawn appropriately based on the data presented.

Reviewer #1: Yes

Reviewer #2: Yes

2. Has the statistical analysis been performed appropriately and rigorously?

Reviewer #1: Yes

Reviewer #2: I Don't Know

3. Have the authors made all data underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data—e.g. participant privacy or use of data from a third party—those must be specified.

Reviewer #1: Yes

Reviewer #2: Yes

4. Is the manuscript presented in an intelligible fashion and written in standard English?

PLOS ONE does not copyedit accepted manuscripts, so the language in submitted articles must be clear, correct, and unambiguous. Any typographical or grammatical errors should be corrected at revision, so please note any specific errors here.

Reviewer #1: Yes

Reviewer #2: No

5. Review Comments to the Author

Please use the space provided to explain your answers to the questions above. You may also include additional comments for the author, including concerns about dual publication, research ethics, or publication ethics. (Please upload your review as an attachment if it exceeds 20,000 characters)

Reviewer #1: Excellent paper. It was not clear if you could discern daily rings on the otoliths. You might want to discuss if you can use rings on otoliths to age the fish without removing them. Also, do you have to stain the fish to use these rings?

Reviewer #2: I have carefully evaluated the manuscript titled "Microtomographic investigation of a large corpus of cichlids". The authors present a substantial collection of tomographic images from cichlids collected in Lake Victoria, Africa. They showcase significant cranial, maxillary, and otolith images from 362 specimens and provide open-source Python notebooks to facilitate the manipulation and extraction of specific parts. I believe that this work represents a significant contribution to the understanding of cichlids and the application of Micro-CT imaging in fish studies. However, I have some suggestions to improve the manuscript:

The introduction section needs improvement. It is too simplistic and lacks informative details about the state of the art and the justification for the work.

Merging the Materials and Methods section with the Results is not a reasonable way to present the work. It would be better to separate them for clarity.

The section on Micro-computed tomographic imaging should be the core of the paper and explained in more detail. The authors have extensive experience scanning 362 fish specimens of different species and sizes. Therefore, a detailed imaging protocol that can assist readers in obtaining new images should be provided. For example, what criteria did the authors use to select the best set of parameters? It is clear and expected that larger fish would have lower resolution (larger voxel size), but how does the relationship between size and parameters work? How was the filter thickness chosen?

The first sentence of the last paragraph of the subsection Micro-computed tomographic imaging is unclear: "While performing the work, a subset of the data was always present on the production system, for working with it (see Preparation for analysis below)". Please provide more precise information.

The authors should revise the entire "Data analysis" subsection to present a more didactic version that helps any reader use the notebooks. Currently, it seems that only Python users with some expertise can understand what needs to be done. Perhaps the authors could provide a guide or tutorial in the GitHub repository.

How was the sanity check performed (as mentioned in the second paragraph of the subsection "Preparation for Analysis")?

In the same paragraph, the authors mentioned that each tomographic dataset contains around 2700 slices, exceeding the available RAM size on an average high-end workstation. Could you clarify if this limitation affected the analysis and its implications?

The Wikipedia citation in the second paragraph of the subsection "Extraction of oral and pharyngeal jaws..." is not clear. Please provide more specific information or replace the citation with a more appropriate reference.

Regarding the sentence "In total, we compiled an overview of 125 specimens with full head morphology, oral jaw, and lower pharyngeal jaw profiles," why was this done only for a subset of the sample? Please explain the rationale.

The results of the subsection "Principal components analysis of skull landmarks" should be presented in a more accessible manner. Consider providing a tutorial or guide for readers to better understand and apply the analysis. As it currently stands, this subsection may be considered irrelevant for the paper.

The procedure for detecting and extracting otoliths in the subsection "Automatic extraction of otoliths" is not clear. Please provide clearer instructions or guidelines for readers using the notebook.

Use the full words, rather than abbreviations, in figure legends for clarity.

In the discussion section, the authors mentioned acquiring high-resolution tomographic datasets of a large collection of cichlids. However, the statement that "the acquired datasets were imaged over a wide-spanning range of voxel size (3.5–50 μm)" is incorrect. The voxel size is specimen-specific, depending on the size of the fish and the chosen parameters. Please clarify this point to accurately represent the imaging process. The finest resolution was obtained only for small fishes, so specific structures of a fish will have the same image resolution throughout the entire specimen.

It would be beneficial to include references in the discussion section to support the arguments and provide a broader context for the findings.

Overall, the study seems to have spanned a considerable time frame. However, the manuscript's content and structure need improvement to reach a wider audience and effectively communicate the significance of the work. The authors have provided a valuable set of open-source Python notebooks, which is commendable and will be highly useful for the scientific community. However, the workflow needs to be better explained to enable readers to follow the procedures accurately.

By addressing these suggestions, the manuscript will become more comprehensive, accessible, and representative of the valuable contribution made by the authors.

6. PLOS authors have the option to publish the peer review history of their article (what does this mean?). If published, this will include your full peer review and any attached files.


If you choose “no”, your identity will remain anonymous but your review may still be made public.


Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy.

Reviewer #1: Yes: [REDACTED]

Reviewer #2: No




[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/. PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step.






In compliance with data protection regulations, you may request that we remove your personal registration details at any time. (Remove my information/details). Please contact the publication office if you have any questions.
