An empty token reaches `Session.new` and creates a session that no request can reuse.

Reject the token before allocating the session. Existing non-empty tokens keep the same path.

`pytest tests/test_session.py::test_rejects_empty_token` failed before the guard and passes with it.

The verification did not cover session reuse on Windows.
