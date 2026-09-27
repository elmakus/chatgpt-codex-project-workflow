# M02Q-T26 prelaunch acceptance correction

Launch inspection found that the exact 23 legacy statusless Results also terminate in historical GREEN reviews whose `acceptance` is path-only. T26 had not yet mutated the product. Requiring literal commit+blob acceptance would therefore leave the recorded OBL-M02Q-03 consumer unservable even after Result provenance support.

The stable Card is corrected before substantive implementation: only inside an explicit valid legacy-Result migration proof, a path-only historical review acceptance may be exact-derived from that review attempt's own immutable locator commit and must resolve the accepted Card path to bytes identical to the current stable Card. This does not weaken normal RF004 behavior and does not permit path-only acceptance for current/unproved Results.

The consumer migration remains a separate downstream outcome; M03 remains unmaterialized.
