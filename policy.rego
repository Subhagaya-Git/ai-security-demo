package security

default allow = false

allow if {
    count(input.results) == 0
}
