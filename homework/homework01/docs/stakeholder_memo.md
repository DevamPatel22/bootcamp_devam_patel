# Stakeholder Memo: Loan Default Risk Prediction

## To

Credit Risk Team / Loan Review Team

## From

Devam Patel

## Subject

Framing a Machine Learning Project to Predict Loan Default Risk

## Context

Many people have difficulty getting approved for loans because they have limited or nonexistent traditional credit histories. This can make them more vulnerable to unfair lenders or loan terms that do not match their repayment ability.

Home Credit’s dataset focuses on this problem by using loan application information and alternative data to estimate whether an applicant is likely to repay a loan.

## Stakeholder Need

The credit risk team needs a way to better estimate repayment risk before making lending decisions. The goal is not only to avoid defaults, but also to avoid rejecting applicants who may actually be capable of repayment.

## Proposed Useful Output

The proposed model would output a probability that a loan applicant will experience repayment difficulty.

This probability could help the loan review team decide whether to:

- approve the applicant
- request additional review
- adjust loan terms
- reject a high-risk application

## Metric

The main model evaluation metric will be ROC AUC, matching the original Home Credit Default Risk competition evaluation. ROC AUC is useful because it evaluates how well the model ranks applicants by risk across classification thresholds.

## Risks and Considerations

- The model must be explainable because lending decisions affect real people.
- Missing or noisy data could reduce model reliability.
- Historical data may contain bias.
- A strong model score does not automatically mean the model is fair or appropriate for real lending decisions.

## Recommendation

Start with a clear baseline model using the main application table, then improve the project by adding joined and aggregated features from related credit-history tables.