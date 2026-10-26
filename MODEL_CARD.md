# Model / system card

## Intended use

Detect artificial assay outliers after correcting plate offsets with explicit reference controls. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Estimate each plate offset using designated controls. Learn a median and MAD-based feature scale from corrected training wells. Score a well by its maximum robust standardized deviation and choose a threshold from a separate normal validation plate.

## Evaluation protocol

Test on a held-out plate containing injected anomalies, keeping anomaly labels outside fitting and threshold selection. Compare with an always-normal baseline.

## Known limits

The readouts and anomalies are mathematical fixtures. Control wells are assumed reliable; missing or contaminated controls invalidate the correction.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Add multivariate covariance methods, control-failure checks, plate drift diagnostics and a licensed assay-QC benchmark.
