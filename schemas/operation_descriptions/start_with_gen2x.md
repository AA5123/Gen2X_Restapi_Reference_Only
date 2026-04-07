Applies all staged Gen2X settings and starts the radio. Set `applyImpinjGen2X` to `true` for the Gen2X configuration to take effect.

> **Important:** Stop the radio before you send this command. Starting while the radio is already running returns an error.

**Workflow:**
1. Configure Gen2X features using the set commands.
2. Verify your configuration with `get_gen2x_config`.
3. Stop the radio if it's running.
4. Send this command with `applyImpinjGen2X: true`.
