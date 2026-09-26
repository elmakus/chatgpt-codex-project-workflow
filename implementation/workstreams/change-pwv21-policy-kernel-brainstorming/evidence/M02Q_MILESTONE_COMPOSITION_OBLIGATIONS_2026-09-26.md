# M02Q milestone composition obligations

Durable record of cross-seam obligations that must resolve before the M02Q
Milestone Review can be GREEN. These are milestone-level obligations, not
Card scope of any single RF seam. Terminal M01/M02/M02R history is preserved;
nothing here rewrites it.

## OBL-M02Q-01 (load-bearing): H017 package / Final composition

Source: independent T18 R01 review,
`evidence/M02Q-T18_REVIEW_R01_2026-09-26.md`:
in an independent fixture, Board-derived Final accepted a complete cleanup
work while `derive_recovery_package_from_board` returned a package without
that cleanup work's Review and evidence. H019 per-work proof is correct; the
H017 target package and Final must compose before M02Q Milestone Review GREEN.

Disposition: separate correction owning the RF011-internal composition seam
between the derived recovery package and the Final gate (package must cover
every accepted cleanup work's Review/evidence, or Final must not accept work
absent from the target package). Explicitly NOT absorbed into P7 order-15
RF001: RF001 owns Board status/result/review/blocker coherence and routing
precedence, not package-contents composition; no Board-coherence binding in
RF001 needs that package content, and absorbing RF011 rework would merge
across required seams. Resolve at the smallest safe downstream boundary
before M02Q Milestone Review; M03 remains blocked until then.

## OBL-M02Q-02 (preservation note): legacy path-only terminal reviews

The current consumer's path-only terminal legacy Review locators fail the
H017/H019 gates until valid RF006 migration provenance is supplied. This is
the separate RF006 migration obligation. Correctly terminal history stays
unchanged; replay only as immutable fixtures/evidence.
