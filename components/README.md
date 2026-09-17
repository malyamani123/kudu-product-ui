# Component implementation boundary

Component specifications are in [02-components.md](../.agents/skills/kudu-product-ui/references/02-components.md).

This draft does not contain a production React/Vue/Streamlit component implementation. There is no installed or published `@kudu/ui` package. Earlier examples such as `<Button variant="primary">` define a desired API, not an import that already works.

Before implementation, inspect the selected product's framework, installed libraries, existing controls, tests, and licensing constraints. Start with Button, Input, Select, Badge, Modal, Table, Search/Filters, Toast/Alert, Navigation, and File Upload. Use mature interaction primitives where appropriate, but replace their styling with approved KUDU tokens rather than importing a visual template.

Keep complex table or document behaviors behind composition and product data contracts. Do not force one large component API onto every product. A component is not complete until its relevant states, keyboard behavior, responsive layout, and RTL behavior are tested.
