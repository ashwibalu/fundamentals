The Bandwidth AI Code Reviewer is designed to assist developers during the pull request review process. The system analyzes repository code and provides additional context that may help developers understand how their changes affect other parts of the project. The reviewer is intended to support human reviewers rather than replace them.

Repository processing begins by examining the files contained in a software project. Files that are not useful for code analysis, such as generated files, dependencies, and binary files, can be removed during the filtering stage. The remaining source files are then passed to the chunking component for further processing.

Chunking divides large source files into smaller pieces that can be processed independently. Breaking files into smaller sections makes it easier for later components of the system to work with specific portions of code. Information about each chunk, such as its source file and location within the file, can also be stored as metadata.

After chunks are created, they can be sent through an embedding model. The embedding model converts the text contained in each chunk into a numerical vector. These vectors provide a mathematical representation of the content and can later be used to compare different pieces of code.

The generated embeddings are stored in a vector database. When the AI reviewer eventually analyzes a pull request, the system can use these stored representations to locate repository code that may be related to the proposed changes. This additional context can then be provided to the review model.

The final goal of the system is to provide useful code review feedback directly to developers. A developer should be able to create a pull request, receive feedback about potential issues, and examine relevant code from other parts of the repository. The developer can then decide whether any changes should be made before the pull request is merged.