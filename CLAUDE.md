# CLAUDE.md

Guidance for Claude Code when working in this repository. Keep this file short and current; Claude reads it at the start of every session.

## Project overview

`acme-api` is a REST API for managing customer orders. It is written in TypeScript (Node 20) with Express, uses PostgreSQL via Prisma, and is deployed as a Docker container.

## Repository layout

- `src/routes/` – Express route handlers, one file per resource
- `src/services/` – business logic; routes should stay thin and call into services
- `src/db/` – Prisma schema and migrations
- `tests/` – Vitest unit and integration tests, mirroring `src/`
- `scripts/` – one-off maintenance scripts (not shipped)

## Common commands

```bash
npm install            # install dependencies
npm run dev            # start the dev server on :3000 with hot reload
npm test               # run all tests
npm test -- path/to/file.test.ts   # run a single test file
npm run lint           # ESLint + Prettier check
npm run typecheck      # tsc --noEmit
npx prisma migrate dev # apply migrations to the local database
```

Before saying a change is done, run `npm run lint`, `npm run typecheck`, and the tests that cover the change.

## Code style

- TypeScript strict mode; avoid `any`. Prefer `unknown` plus a type guard.
- Use named exports, not default exports.
- Async code uses `async`/`await`, never raw `.then()` chains.
- Errors: throw `AppError` (from `src/errors.ts`) with an HTTP status; never return error objects.
- Keep functions small. If a function needs a comment explaining what it does, consider splitting it.
- Match the existing style of the file you are editing.

## Testing

- Every new service function gets a unit test.
- Every new route gets an integration test in `tests/routes/`.
- Integration tests use the test database from `docker compose up db-test`; never point tests at the dev database.
- Do not skip or delete failing tests to make the suite pass. Fix the cause or ask.

## Git and pull requests

- Branch names: `feature/<short-description>` or `fix/<short-description>`.
- Commit messages: imperative mood, under 72 characters for the subject line (e.g. "Add order cancellation endpoint").
- One logical change per PR. Include a short description of what changed and how it was tested.
- Never commit `.env` files, secrets, or generated files in `dist/`.

## Things to avoid

- Do not edit files in `src/db/migrations/` that have already been merged; create a new migration instead.
- Do not add new dependencies without mentioning why in the PR description.
- Do not change public API response shapes without updating `docs/api.md`.

## Gotchas

- The `orders.total` column is stored in cents (integer), not dollars.
- `npm run dev` requires a running Postgres; start it with `docker compose up db`.
- Timezones: all timestamps are stored and returned in UTC.
