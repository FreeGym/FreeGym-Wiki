# How Accurate Is Distance From a Wearable?

Distance from a wearable is not one measurement. It is two different outputs sharing one column name: outdoor GNSS/GPS path length and indoor accelerometer/stride-length distance. Outdoor validation studies evaluate positioning-enabled sport watches on courses and field routes, while treadmill validation studies evaluate distance generated without GNSS, usually through step count and step-length models. That distinction matters because an exported column called `distance` can be treated as a stable measurement even when the measurement pathway is absent. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))

## Verdict

|Metric|Verdict|Why|
|---|--:|---|
|`distance` as a generic exported field|**Exclude**|The same label can mean outdoor GNSS path length or treadmill stride-model distance, and validation findings differ sharply by pathway and setting. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300))|
|Outdoor GNSS/GPS distance with source context preserved|**Include**|Peer-reviewed field studies support useful accuracy for outdoor running and cycling distance, especially on road or open-sky courses, but not as a context-free metric. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))|
|Outdoor GNSS/GPS distance after context is stripped|**Exclude**|The evidence depends on conditions, device, route geometry, and signal environment. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675); [Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf))|
|Indoor/treadmill wearable distance|**Exclude**|Validation studies show accurate step counts can still produce poor distance estimates because distance is modeled from stride length. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))|
|Pace derived from included outdoor GNSS distance and elapsed time|**Include**|Pace can be calculated from elapsed time and validated outdoor GNSS distance when the upstream distance source and activity context are preserved. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880))|
|Indoor/treadmill pace from wearable distance|**Exclude**|It inherits the same stride-length distance error. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))|
|Wearable calorie/energy-expenditure estimates|**Exclude**|Systematic reviews show consumer wearable energy expenditure is not accurate enough for individual-level export. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Argent et al., 2022](https://link.springer.com/article/10.1007/s40279-022-01665-4))|
|Wearable VO2max/cardiorespiratory-fitness estimate|**Exclude**|Meta-analysis shows large individual-level limits of agreement even when group mean bias is small. ([Molina-Garcia et al., 2022](https://link.springer.com/article/10.1007/s40279-021-01639-y))|
|Multi-band or multi-GNSS capability|**Include as metadata only**|GNSS hardware and mode can help stratify confidence, but the cited smartwatch evidence supports context-specific positioning performance rather than a universal distance-accuracy guarantee. ([Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf))|

## What outdoor GNSS distance supports

Outdoor GNSS distance is the strongest version of wearable distance because positioning-enabled watches estimate distance from recorded position fixes rather than from stride-length inference. That makes it closer to a geometric path estimate than indoor distance, but it is still affected by signal obstruction, multipath reflection, receiver and antenna constraints, route geometry, and device processing. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf))

In a marathon-event field study, GPS sport watches were close to the official race distance: for the half marathon, GPS sport watches had a mean absolute error of 0.12 km, or about 0.6 percent, while mobile-phone app records had a larger mean absolute error of 0.35 km, or about 1.7 percent. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/)) A separate ultramarathon race study comparing GPS sport-watch distance with measured race segments found brand/model error ranges of about 0.6 ± 0.3 percent to 1.9 ± 1.5 percent. ([Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880))

Those race studies support outdoor GNSS distance for road running under favorable conditions. They do not support treating every wearable distance value as equally accurate. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880))

A controlled validation of eight positioning-enabled sport watches found worse performance in more difficult environments. Across watches, overall mean absolute percentage error ranged from 3.2 to 6.1 percent; in forest and urban conditions, watches tended to underestimate distance, with condition-specific errors reaching about 3.5 to 8.9 percent. The same study reported better performance in open track/field conditions, where errors were generally below 5 percent. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/)) This study should be interpreted with its funding context: Polar Electro partly funded the experiment and provided the Polar and non-Polar products, although the authors stated that Polar had no influence on data collection, analysis, results, or publication. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/))

A 2024 validation of ten smartwatches for triathlon training also shows why the 1 to 2 percent claim is too broad. Distance error varied by device and activity: mean absolute percentage error ranged from 0.8 to 12.1 percent on a 4000 m track run, 0.2 to 7.5 percent on a hilly outdoor run, and 0.0 to 4.2 percent on a road cycling course. The authors reported no external funding and no conflicts of interest. ([Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

The practical conclusion is clear: outdoor GNSS distance can be included when the export preserves that it is outdoor GNSS distance. The column should not be called simply `distance` unless the activity mode, source, and context are also available. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

## The race-course comparison does not rescue generic distance

The strongest outdoor evidence comes from comparisons against race or measured-course distances. That is enough to support training use in similar contexts, but it is not enough to say that GPS distance is essentially correct in all recreational or competitive use. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880); [Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/))

The field evidence supports this narrower claim: on road races or open routes, many GPS sport watches are close enough for training mileage and pacing decisions. It does not support this broader claim: wearable distance is accurate regardless of route type, hardware, sport mode, signal environment, or export context. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880); [Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

That gap is the main finding. Wearable brands often market distance as one stable output. The sensor evidence supports a narrower metric: outdoor GNSS-derived path length under known conditions. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300))

## Indoor and treadmill distance are not direct measurements

Indoor distance is a different metric. In treadmill validation studies, wearables can count steps accurately while producing poor distance estimates, which shows that indoor distance is not validated by step-count accuracy alone. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))

The Fitbit Inspire 2 treadmill study found strong step-count agreement but poor distance accuracy. In 30 college students walking on a treadmill at 5.5 km/h for 30 minutes, step count had high validity, but distance had a mean absolute percentage error of about 10.5 percent and was underestimated. The authors proposed that a plausible explanation was that Fitbit calculated distance from step count and step length. They reported no financial support and no conflicts of interest. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300))

An earlier treadmill validation of the Fitbit One reached the same practical conclusion: step count was accurate, but distance output was invalid using default calculations, with relative distance error reported as high as 39.6 percent. The authors reported no external financial support. ([Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))

A 2022 systematic review of wrist-worn activity trackers also shows that distance and speed have a thin validation base compared with more commonly studied outcomes such as steps, heart rate, and energy expenditure. Distance was evaluated in only a small subset of included studies, and the review found substantial heterogeneity across devices, protocols, and outcomes. The authors declared no conflicts of interest. ([Germini et al., 2022](https://www.jmir.org/2022/1/e30791/))

The verdict is therefore binary: wearable indoor/treadmill distance is exclude. It may be useful as a rough personal estimate on the device screen, but it should not be exported as a ground-truth distance field. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726); [Germini et al., 2022](https://www.jmir.org/2022/1/e30791/))

## Multi-band GPS and multi-GNSS mode are useful metadata, not standalone verdicts

GNSS hardware and mode can matter, but the peer-reviewed wearable evidence cited here does not justify using multi-band or multi-GNSS status as a simple include/exclude switch for distance accuracy. ([Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf); [Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/))

A field-positioning study of a Garmin Fenix 7X Solar Sapphire found that multi-GNSS improved static horizontal and vertical accuracy compared with GPS-only under some conditions, but kinematic results were not uniformly better. In motion, the multi-GNSS configuration did not consistently improve horizontal RMSE compared with GPS-only, and the authors emphasized that smartwatch positioning remains limited by antenna constraints, multipath, signal noise, speed, and satellite configuration. ([Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf)) The test watch in that study was provided by a technical-device company, which should be treated as material support. ([Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf))

So the correct pipeline treatment is: store GNSS hardware and mode as metadata, not as proof that a distance value is accurate. The cited smartwatch evidence directly supports multi-GNSS as a positioning factor, not a universal rule that multi-band distance is accurate. The metric that may be included is outdoor GNSS distance with source and context preserved. ([Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf); [Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

## Distance error directly affects pace, and related modeled outputs are not export-safe

Pace is mechanically downstream of distance because speed and pace are calculated from distance and time. If a device underestimates a treadmill session's distance by 10 percent over the same elapsed time, it also underestimates speed by 10 percent and makes pace look slower. That is not a separate sensor failure; it is simple propagation from a bad upstream distance value. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))

Energy expenditure is less defensible as an exported ground-truth metric. A systematic review of commercially available wearables found that energy-expenditure estimates were not accurate for any evaluated brand. In controlled studies, fewer than 10 percent of comparisons were within ±3 percent of the criterion measure, and in free-living studies only 18 percent were within ±10 percent. The review also noted that many brands do not publish their energy-expenditure algorithms. One author was employed by Garmin during the publication process after the study was completed; the other authors declared no conflicts. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/))

The INTERLIVE expert statement on wearable energy-expenditure validation reached the same direction of concern: validation methods are heterogeneous, intended use and target population matter, and free-living validation is limited. That statement was partly funded by Huawei Technologies, and the authors declared no conflicts of interest. ([Argent et al., 2022](https://link.springer.com/article/10.1007/s40279-022-01665-4))

Wearable VO2max estimates also fail the export test. A systematic review and meta-analysis found that exercise-based wearable VO2max estimates had small average bias, but individual-level limits of agreement were wide, roughly -9.92 to +9.74 mL/kg/min. Resting algorithms overestimated VO2max on average, and the included studies had some concerns or high risk of bias. The study was produced by the INTERLIVE network, which included Huawei as an industry partner, and it was partly funded by Huawei Technologies Oy. ([Molina-Garcia et al., 2022](https://link.springer.com/article/10.1007/s40279-021-01639-y))

A 2024 living umbrella review of systematic reviews evaluated consumer wearable accuracy across health measurements, reinforcing that accuracy should be judged metric by metric rather than assumed from the device as a whole. ([Doherty et al., 2024](https://link.springer.com/article/10.1007/s40279-024-02077-2))

That means the indoor-distance problem is not isolated. It can silently contaminate derived outputs, especially when indoor and outdoor sessions are mixed in the same longitudinal dataset. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Molina-Garcia et al., 2022](https://link.springer.com/article/10.1007/s40279-021-01639-y))

## Competing claims resolved

### Claim 1: Outdoor GPS distance from a modern multi-band wearable is accurate enough for nearly any recreational and most competitive use.

**Verdict: Partly supported, but too broad.**

Outdoor GNSS distance is strong enough to include when the export preserves outdoor GNSS context. Race and field studies show many GPS sport watches perform well on road or open routes, often around 1 to 2 percent error in favorable settings. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880)) But validation studies also show larger errors in forest, urban, track, hilly, and device-specific conditions. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

**Pipeline verdict:** include `outdoor_gnss_distance_m`; exclude generic `distance`.

### Claim 2: Indoor and treadmill distance should be treated as estimates, not measurements.

**Verdict: Supported.**

Treadmill studies show that wearables can count steps accurately while producing poor distance estimates. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726)) The mechanism is also weaker: without GNSS, the device must infer distance rather than measure outdoor path length from position fixes. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300))

**Pipeline verdict:** exclude wearable indoor/treadmill distance.

### Claim 3: Indoor distance error propagates silently into other metrics.

**Verdict: Supported for pace; exclusion still supported for calories and VO2max.**

Pace inherits distance error directly. Energy expenditure and VO2max are less transparent because algorithms are often proprietary or model-dependent, but systematic reviews show that these outputs are not accurate enough for individual-level export. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Molina-Garcia et al., 2022](https://link.springer.com/article/10.1007/s40279-021-01639-y))

**Pipeline verdict:** exclude wearable calories, indoor pace, and wearable VO2max as ground-truth metrics.

### Claim 4: Multi-band GPS is now the meaningful differentiator in wearable distance accuracy.

**Verdict: Not supported as a standalone rule.**

GNSS hardware matters, but peer-reviewed evidence does not support a simple multi-band equals accurate rule across brands, activities, and environments. Device model, antenna design, route geometry, sampling behavior, signal obstruction, and processing still matter. ([Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf); [Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

**Pipeline verdict:** include GNSS hardware/mode as metadata; exclude brand-level or multi-band-only accuracy claims.

## Quick reference values

- GPS sport watches in a half-marathon field study: mean absolute error about 0.12 km, or 0.6 percent. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/))

- GPS sport watches in a 56 km ultramarathon: brand/model error about 0.6 ± 0.3 percent to 1.9 ± 1.5 percent. ([Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880))

- Eight positioning-enabled sport watches across varied environments: overall mean absolute percentage error about 3.2 to 6.1 percent; forest and urban conditions worse than open areas. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/))

- Ten smartwatches in triathlon-relevant testing: distance error ranged from 0.8 to 12.1 percent on track runs, 0.2 to 7.5 percent on hilly runs, and 0.0 to 4.2 percent on road cycling. ([Jacko et al., 2024](https://www.mdpi.com/1424-8220/24/14/4675))

- Fitbit Inspire 2 treadmill walking: step count valid, distance mean absolute percentage error about 10.5 percent. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300))

- Fitbit One treadmill walking: step count valid, distance invalid using default calculations, with relative error reported as high as 39.6 percent. ([Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))


## Practical interpretation

Use this schema:

|Export field|Verdict|Basis|
|---|--:|---|
|`outdoor_gnss_distance_m`|**Include**|Include only when source and outdoor activity context are preserved. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880); [Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/))|
|`outdoor_gnss_distance_trend`|**Include**|Include only for preserved outdoor GNSS sessions, where the underlying distance metric is valid enough to use. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880))|
|`outdoor_gnss_pace` derived from included distance and elapsed time|**Include**|Pace is acceptable only when the upstream distance source is acceptable. ([Pobiruchin et al., 2017](https://mhealth.jmir.org/2017/2/e24/); [Johansson et al., 2020](https://journals.sagepub.com/doi/10.1177/1747954119899880))|
|`gnss_hardware_mode`, `device_model`, `activity_type`, `indoor_outdoor_flag`|**Include as metadata**|These fields preserve context needed to interpret distance accuracy. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Alkan et al., 2026](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf))|
|`distance` without source context|**Exclude**|Generic distance hides whether the value came from outdoor GNSS or indoor stride modeling. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300))|
|`watch_treadmill_distance_m`|**Exclude**|Treadmill validation studies show poor distance accuracy despite accurate step counts. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))|
|`indoor_distance_m` from wearable|**Exclude**|Indoor wearable distance has a weaker validation base and can be inaccurate when modeled from steps and stride length. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Germini et al., 2022](https://www.jmir.org/2022/1/e30791/))|
|`indoor_pace` from wearable distance|**Exclude**|It inherits the indoor distance error. ([Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Takacs et al., 2014](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726))|
|`calories_burned` or `active_calories` from wearable|**Exclude**|Consumer wearable energy-expenditure estimates are not accurate enough for individual-level export. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Argent et al., 2022](https://link.springer.com/article/10.1007/s40279-022-01665-4))|
|`vo2max_estimate` from wearable|**Exclude**|Wearable VO2max estimates have wide individual-level limits of agreement. ([Molina-Garcia et al., 2022](https://link.springer.com/article/10.1007/s40279-021-01639-y))|
|Proprietary recovery/readiness/fitness composites using distance|**Exclude**|Proprietary or undocumented modeled outputs are not validated as transparent distance-derived ground truth. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Doherty et al., 2024](https://link.springer.com/article/10.1007/s40279-024-02077-2))|

The clean conclusion is this: outdoor GNSS distance is a valid narrow metric; wearable distance is not a valid broad metric. The export should preserve the narrow claim or drop the field. ([Gilgen-Ammann et al., 2020](https://mhealth.jmir.org/2020/6/e17118/); [Cheung et al., 2025](https://journals.sagepub.com/doi/10.1177/22130683251337300); [Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Molina-Garcia et al., 2022](https://link.springer.com/article/10.1007/s40279-021-01639-y))

## References

- Pobiruchin M, Suleder J, Zowalla R, Wiesner M. [Accuracy and Adoption of Wearable Technology Used by Active Citizens: A Marathon Event Field Study](https://mhealth.jmir.org/2017/2/e24/). _JMIR mHealth and uHealth_. 2017;5(2):e24. DOI: [10.2196/mhealth.6395](https://doi.org/10.2196/mhealth.6395).

- Johansson RE, Adolph ST, Swart J, Lambert MI. [Accuracy of GPS sport watches in measuring distance in an ultramarathon running race](https://journals.sagepub.com/doi/10.1177/1747954119899880). _International Journal of Sports Science & Coaching_. 2020;15(2):212-221. DOI: [10.1177/1747954119899880](https://doi.org/10.1177/1747954119899880).

- Gilgen-Ammann R, Schweizer T, Wyss T. [Accuracy of Distance Recordings in Eight Positioning-Enabled Sport Watches: Instrument Validation Study](https://mhealth.jmir.org/2020/6/e17118/). _JMIR mHealth and uHealth_. 2020;8(6):e17118. DOI: [10.2196/17118](https://doi.org/10.2196/17118).

- Jacko T, et al. [Validity of Current Smartwatches for Triathlon Training: How Accurate Are Heart Rate, Distance, and Swimming Readings?](https://www.mdpi.com/1424-8220/24/14/4675). _Sensors_. 2024;24(14):4675. DOI: [10.3390/s24144675](https://doi.org/10.3390/s24144675).

- Alkan RM, et al. [GNSS Positioning Performance Analysis of Smartwatches](https://isprs-archives.copernicus.org/articles/XLVIII-4-W17-2025/21/2026/isprs-archives-XLVIII-4-W17-2025-21-2026.pdf). _The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences_. 2026.

- Cheung YS, et al. [Validity of Fitbit Inspire 2 in Step Count and Distance Measurement During Treadmill Walking](https://journals.sagepub.com/doi/10.1177/22130683251337300). 2025. DOI: [10.1177/22130683251337300](https://doi.org/10.1177/22130683251337300).

- Takacs J, Pollock CL, Guenther JR, Bahar M, Napier C, Hunt MA. [Validation of the Fitbit One activity monitor device during treadmill walking](https://www.sciencedirect.com/science/article/abs/pii/S1440244013004726). _Journal of Science and Medicine in Sport_. 2014;17(5):496-500. DOI: [10.1016/j.jsams.2013.10.241](https://doi.org/10.1016/j.jsams.2013.10.241).

- Germini F, et al. [Accuracy and Acceptability of Wrist-Wearable Activity-Tracking Devices: Systematic Review of the Literature](https://www.jmir.org/2022/1/e30791/). _Journal of Medical Internet Research_. 2022;24(1):e30791. DOI: [10.2196/30791](https://doi.org/10.2196/30791).

- Fuller D, et al. [Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review](https://mhealth.jmir.org/2020/9/e18694/). _JMIR mHealth and uHealth_. 2020;8(9):e18694. DOI: [10.2196/18694](https://doi.org/10.2196/18694).

- Doherty C, et al. [Keeping Pace with Wearables: A Living Umbrella Review of Systematic Reviews Evaluating the Accuracy of Consumer Wearable Technologies in Health Measurement](https://link.springer.com/article/10.1007/s40279-024-02077-2). _Sports Medicine_. 2024. DOI: [10.1007/s40279-024-02077-2](https://doi.org/10.1007/s40279-024-02077-2).

- Molina-Garcia P, et al. [Validity of Estimating the Maximal Oxygen Consumption by Consumer Wearables: A Systematic Review with Meta-analysis and Expert Statement of the INTERLIVE Network](https://link.springer.com/article/10.1007/s40279-021-01639-y). _Sports Medicine_. 2022;52:1577-1597. DOI: [10.1007/s40279-021-01639-y](https://doi.org/10.1007/s40279-021-01639-y).

- Argent R, et al. [Recommendations for Determining the Validity of Consumer Wearables and Smartphones for the Estimation of Energy Expenditure: Expert Statement and Checklist of the INTERLIVE Network](https://link.springer.com/article/10.1007/s40279-022-01665-4). _Sports Medicine_. 2022;52:1817-1832. DOI: [10.1007/s40279-022-01665-4](https://doi.org/10.1007/s40279-022-01665-4).