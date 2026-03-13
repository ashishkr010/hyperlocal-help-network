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
Priya just moved in and needs help assembling furniture. She posts a request, Rahul three streets away sees it, offers to help, and gets a 5-star review after. His trust score goes up in the community.

**Elderly care**
An elderly man needs medicines picked up. His daughter posts an urgent request on his behalf. A nearby volunteer picks it up within the hour.

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Alembic (migrations)
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

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /users/ | Create a user |
| POST | /requests/ | Post a help request |
| GET | /requests/ | List requests (filter by pincode) |
| POST | /offers/ | Make an offer to help |
| PATCH | /offers/{id}/accept | Accept an offer |
| PATCH | /offers/{id}/cancel | Cancel an offer |
| POST | /reviews/ | Leave a review |
