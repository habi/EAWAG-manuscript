---
title: Answer to reviewers of PONE-D-23-10896 (Microtomographic investigation of a large corpus of cichlids)
author: David Haberthür
date: 3.7.2023
---

# Review Comments to the Author

> Reviewer #1: Excellent paper.
> It was not clear if you could discern daily rings on the otoliths.
> You might want to discuss if you can use rings on otoliths to age the fish without removing them.
> Also, do you have to stain the fish to use these rings?

The data shown in this manuscript is from unstained specimen.
They have been stored in ethanol and scanned in wet foam, but *no* staining was applied.
Since we here only focus on the morphology of the skull and teeth such a staining was not necessary to extract the needed data from the tomographic images.
Growth rings would most probably be visible in the analyzed specimens, but only if some staining is applied, e.g. by storing the fish in Lugol solution.
Since this was *not* the focus of the present study we did not do this here.

To use the data on both growth rings and volume of the otoliths one would have to calibrate this first to be able to extract age estimates.
I.e. one would have to make a simple growth experiment where a number of fish with known age are euthanized, tomographically imaged and then the volume of their extracted otoliths is correlated with their age.
Such a calibration would match size and volume of both the (lab-raised) fish and the otoliths with the age of the fish.
This data could then be used to estimate the age of fishes collected in the wild.

> Reviewer #2: I have carefully evaluated the manuscript titled "Microtomographic investigation of a large corpus of cichlids". The authors present a substantial collection of tomographic images from cichlids collected in Lake Victoria, Africa. They showcase significant cranial, maxillary, and otolith images from 362 specimens and provide open-source Python notebooks to facilitate the manipulation and extraction of specific parts. I believe that this work represents a significant contribution to the understanding of cichlids and the application of Micro-CT imaging in fish studies. However, I have some suggestions to improve the manuscript:

> The introduction section needs improvement. It is too simplistic and lacks informative details about the state of the art and the justification for the work.

> Merging the Materials and Methods section with the Results is not a reasonable way to present the work.
> It would be better to separate them for clarity.

The manuscript is focused on the method on how to acquire and assess tomographic datasets of a large corpus of cichlids.
Especially for the image processing part, the method and results are highly intertwined as the Python code directly delivers the results.
We believe that the approach we chose here here is the most appropriate way to present the whole data data acquisition and analysis pipeline and kindly ask the reviewer to accept our choice.

> The section on Micro-computed tomographic imaging should be the core of the paper and explained in more detail. The authors have extensive experience scanning 362 fish specimens of different species and sizes. Therefore, a detailed imaging protocol that can assist readers in obtaining new images should be provided. For example, what criteria did the authors use to select the best set of parameters? It is clear and expected that larger fish would have lower resolution (larger voxel size), but how does the relationship between size and parameters work? How was the filter thickness chosen?

> The first sentence of the last paragraph of the subsection Micro-computed tomographic imaging is unclear: "While performing the work, a subset of the data was always present on the production system, for working with it (see Preparation for analysis below)".
> Please provide more precise information.

We are sorry for the imprecise description of the data archival and copying process.
The last paragraph of [this section](https://habi.github.io/EAWAG-manuscript/#micro-computed-tomographic-imaging) was expanded and hopefully improved.

> The authors should revise the entire "Data analysis" subsection to present a more didactic version that helps any reader use the notebooks. Currently, it seems that only Python users with some expertise can understand what needs to be done. Perhaps the authors could provide a guide or tutorial in the GitHub repository.

> How was the sanity check performed (as mentioned in the second paragraph of the subsection "Preparation for Analysis")?

> In the same paragraph, the authors mentioned that each tomographic dataset contains around 2700 slices, exceeding the available RAM size on an average high-end workstation. Could you clarify if this limitation affected the analysis and its implications?

<!-- Not that *one* single dataset exceeds the RAM on a workstation, but *all* datasets together do -->

> The Wikipedia citation in the second paragraph of the subsection "Extraction of oral and pharyngeal jaws..." is not clear.
>Please provide more specific information or replace the citation with a more appropriate reference.

The Wikipedia citation to a [date-specific version of the `Nrrd` article on Wikipedia](https://w.wiki/5mBK) was not correctly expanded by our manuscript preparation system.
We replaced the Wikipedia link with a more appropriate link to [the `Nrrd` format definition](https://teem.sourceforge.net/nrrd/format.html).

> Regarding the sentence "In total, we compiled an overview of 125 specimens with full head morphology, oral jaw, and lower pharyngeal jaw profiles," why was this done only for a subset of the sample? Please explain the rationale.

> The results of the subsection "Principal components analysis of skull landmarks" should be presented in a more accessible manner. Consider providing a tutorial or guide for readers to better understand and apply the analysis. As it currently stands, this subsection may be considered irrelevant for the paper.

> The procedure for detecting and extracting otoliths in the subsection "Automatic extraction of otoliths" is not clear. Please provide clearer instructions or guidelines for readers using the notebook.

> Use the full words, rather than abbreviations, in figure legends for clarity.

Abbreviations in the legends have been written-out (except SI units).
Additionally we added a bit of background information on the specimen to the legend of Fig. 1.

> In the discussion section, the authors mentioned acquiring high-resolution tomographic datasets of a large collection of cichlids. However, the statement that "the acquired datasets were imaged over a wide-spanning range of voxel size (3.5–50 μm)" is incorrect. The voxel size is specimen-specific, depending on the size of the fish and the chosen parameters. Please clarify this point to accurately represent the imaging process. The finest resolution was obtained only for small fishes, so specific structures of a fish will have the same image resolution throughout the entire specimen.

> It would be beneficial to include references in the discussion section to support the arguments and provide a broader context for the findings.

> Overall, the study seems to have spanned a considerable time frame. However, the manuscript's content and structure need improvement to reach a wider audience and effectively communicate the significance of the work. The authors have provided a valuable set of open-source Python notebooks, which is commendable and will be highly useful for the scientific community. However, the workflow needs to be better explained to enable readers to follow the procedures accurately.

> By addressing these suggestions, the manuscript will become more comprehensive, accessible, and representative of the valuable contribution made by the authors.
