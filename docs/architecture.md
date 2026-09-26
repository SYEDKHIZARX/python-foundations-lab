# Architecture

The package separates domain objects and validation from adapters such as the CLI
and file persistence. Tests target the domain boundary so storage can evolve.
