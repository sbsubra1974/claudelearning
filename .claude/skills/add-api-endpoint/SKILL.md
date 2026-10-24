---
name: add-api-endpoint
description: Add a new REST endpoint to the API, with route, service, validation, tests and docs. Use when the user asks to add, create or expose a new API route or endpoint.
---

# Add an API endpoint

Follow these steps to add a new endpoint in a way that matches the rest of the codebase.

## 1. Clarify the contract

Before writing code, make sure you know:

- HTTP method and path (e.g. `POST /orders/:id/cancel`)
- Request body and query parameters, with types
- Response shape and status codes, including error cases
- Who is allowed to call it (auth requirements)

If any of these are unclear, state your assumption and continue with the most likely reading.

## 2. Add the service function

- Put the business logic in `src/services/<resource>.service.ts`.
- Throw `AppError` with an HTTP status for expected failures (not found, conflict, forbidden).
- Keep database access inside the service, not the route.

## 3. Add the route

- Add the handler in `src/routes/<resource>.routes.ts`.
- Validate input with the existing `zod` schemas pattern; put new schemas in `src/schemas/`.
- The handler should only parse input, call the service, and send the response.

## 4. Write tests

- Unit test the service in `tests/services/`, covering the happy path and each error case.
- Integration test the route in `tests/routes/`, checking status codes and response body.
- Run: `npm test -- tests/services/<resource> tests/routes/<resource>`

## 5. Update docs

- Add the endpoint to `docs/api.md` with an example request and response.

## 6. Verify

Run all of these and fix any failures before reporting done:

```bash
npm run lint
npm run typecheck
npm test
```

## Checklist

- [ ] Service function with error handling
- [ ] Route with input validation
- [ ] Unit and integration tests passing
- [ ] `docs/api.md` updated
- [ ] Lint and typecheck clean
