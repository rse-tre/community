# Topic: Data Pipelines for Ingress and Egress

**Session 1, Room 2**

- Chair: Arron Lacey

## Prompts

- Challenges building data pipelines?
- Automation / Reproducibility

## Notes

- **Challenges**

  - Data Quality: creating one solution to ingest different datasets / schemas
  - Different date formats
  - Limits of normality in data
  - Need to harmonise data
    - Should this happen before data arrives in TREs?
    - Does it need to happen inside a TRE (ie, can it typically be done at schema level or does it require sight of aggregate data? record-level data?)
  - Instrument level

- **Automation / Reproducibility**
  - Introduce common standards i.e. BIDS, NIFTI, DICOM Need to consult with domain experts.
    - Can TRE operators (information governance authorities?) require data providers to send data only in a set number of formats? (like data depositories do)
  - With increased processes through data pipeline you can introduce more error in the final output
