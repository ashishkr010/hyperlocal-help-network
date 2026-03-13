# Hyperlocal Help Network

A community platform where people within a locality help each other — no money, just goodwill.

## What it does

- Neighbors post help requests (tasks, errands, skill sharing)
- Others nearby offer to help
- Offers can be accepted or declined
- After the task, the requester leaves a review
- Trust scores build up over time based on reviews

## Use Cases

**New neighbor needs help**
Priya just moved in and needs help assembling furniture. She registers, posts a request, Rahul three streets away logs in, offers to help, and gets a 5-star review after. His trust score goes up in the community.

**Elderly care**
An elderly man needs medicines picked up. His daughter creates an account, posts an urgent request on his behalf. A verified nearby user picks it up within the hour.

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Alembic (migrations)
- JWT authentication (python-jose + passlib)
- Loguru (logging)

## Running locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up .env
echo "DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/hyperlocal" > .env

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`

## Auth flow

1. `POST /auth/register` — create an account
2. `POST /auth/login` — get a JWT token
3. Use the token as a Bearer header on protected endpoints

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /auth/register | No | Create account |
| POST | /auth/login | No | Get JWT token |
| GET | /users/ | No | List users |
| GET | /users/{id} | No | Get user + trust score |
| POST | /requests/ | Yes | Post a help request |
| GET | /requests/ | No | List requests (filter by pincode) |
| GET | /requests/{id} | No | Get request by ID |
| PATCH | /requests/{id}/status | Yes | Update request status |
| POST | /offers/ | Yes | Make an offer to help |
| PATCH | /offers/{id}/accept | Yes | Accept an offer |
| PATCH | /offers/{id}/cancel | Yes | Cancel an offer |
| POST | /reviews/ | Yes | Leave a review (updates trust score) |
