package security

# Default decision is to block deployment
default allow = false

# Allow deployment ONLY IF there are zero findings
allow = true if {
    count(input.results) == 0
}
