# Crash test all basic actions.
(do_nothing)

(debug-message "File actions")
(new-file)
# Set file name procedurally
(open-file)
(save-file)
(save-as-file)

(debug-message "Edit actions")
# Place some objects to act on.
(cut)
(copy)
(paste)

# Crash test set icon size to x calls.
(icon16)
(icon24)
(icon32)
(icon48)
(icon64)
(icon128)

