**Description:**
Enables TagFocus feature so tags that have already been inventoried remain silent in subsequent inventory rounds, allowing the reader to focus exclusively on new or unread tags.

**Usage:**
Send this command to activate TagFocus on the reader. Once enabled, any tag that has been successfully read in the current session (S1) will stop responding to subsequent inventory rounds. This dramatically improves read rates in dense tag environments by eliminating duplicate reads and concentrating RF energy on newly encountered tags. TagFocus remains active until explicitly disabled or the reader is stopped.

**Parameters:**
- `enabled` (boolean): Set to `true` to enable TagFocus feature
