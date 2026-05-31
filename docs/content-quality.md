# Content Quality Reference

## General Writing Standard

Write concrete, domain-specific text. Avoid filler phrases that could fit any project.

Each section should answer:

- what problem exists in the subject area;
- why the current process/tools are insufficient;
- what requirements follow from that;
- what design decision follows from the requirements;
- how the implemented software satisfies the design;
- how tests prove the behavior.

Use local artifacts whenever possible: code, database models, templates, screenshots, test files, README, configuration, packaging scripts, and real output files.

## Competitor And Analog Analysis

Do not write generic competitor paragraphs.

For each analogous tool/product include:

- purpose;
- relevant features;
- what fits the target subject area;
- what does not fit;
- screenshot or official product page image when appropriate;
- short conclusion.

Comparison criteria should be tied to the actual system goals. For a document/report system, criteria may include:

- import of source data;
- unified storage of counterparties/requisites;
- templates;
- generated document types;
- links between generated documents;
- local/offline operation;
- archive/history;
- user editing before generation;
- compatibility with office formats.

## Requirements

Functional requirements should be supported by use cases, not only a flat list.

Include:

- use case diagram;
- actors;
- functional requirements table;
- use case specification tables;
- nonfunctional requirements table.

A use case specification should contain:

- goal;
- actor;
- precondition;
- main scenario;
- alternative scenarios;
- result.

Nonfunctional requirements should connect to design choices:

- reliability;
- local storage;
- data integrity;
- usability;
- maintainability;
- extensibility;
- compatibility;
- security;
- performance.

## Design Content

Design text must explain decisions, not merely name technologies.

For each design decision state:

- requirement or problem that caused it;
- selected solution;
- reason for selection;
- consequence for implementation.

Useful design diagrams:

- use case for functional requirements;
- activity for workflows;
- component for architecture;
- class/ER for data model;
- sequence for interactions;
- deployment for runtime environment.

Use UML-compliant diagrams where UML is expected.

## Development Content

Development section should map design to real implementation.

Include:

- source tree/module structure;
- database models and migrations;
- core algorithms/services;
- document/report generation;
- user interface;
- storage/archive/files;
- launch/build/package.

Mention real files/classes/services. Avoid long pasted source code in the main text.

## Testing Content

Testing section should focus on risk and evidence.

Include:

- testing approach and quality criteria;
- domain risks and verification methods;
- functional test cases;
- module/integration test mapping;
- manual UI checklist when GUI is involved;
- screenshot or summarized output of actual test run;
- conclusion about coverage and remaining limitations.

Test tables should include expected and actual result.

## Planning And Budget

If following the priority example, include planning and conditional budget in section 4.

Include:

- project stages;
- work content;
- estimated hours;
- stage result;
- conditional cost calculation;
- Gantt chart or calendar table.

Keep calculations plausible and transparent.

## Sources

Use sources that are actually useful to the text.

Prefer:

- official technology documentation for libraries/frameworks/tools;
- official product pages for competitors;
- textbooks, standards, or reliable articles for theory;
- methodical documents for ВКР/GOST requirements if available.

For electronic resources include URL and access date.

Do not pad the list with unrelated sources.

## Appendices

Appendices should offload bulky but useful material:

- glossary;
- database attribute specification;
- selected code listings;
- selected test listings;
- additional screenshots;
- large tables.

Each appendix must have a purpose. Do not include the entire project source tree.
