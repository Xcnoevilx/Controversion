# Controversion Data Model

## Purpose

This document defines the main types of information stored by Controversion and how they relate to each other.

The initial design should remain simple enough for an MVP while allowing the platform to expand later.

---

# 1. Topics

A Topic represents a controversy or disputed subject.

Fields:

- id
- title
- slug
- summary
- category
- status
- created_at
- updated_at
- created_by

Example:

Topic: JFK Assassination

A topic can contain multiple claims.

---

# 2. Claims

A Claim is a specific statement that can be investigated.

Fields:

- id
- topic_id
- claim_text
- description
- confidence_level
- confidence_reasoning
- created_at
- updated_at

Example:

Claim:
Lee Harvey Oswald acted alone.

Another claim under the same topic could examine whether additional people were involved.

---

# 3. Evidence

Evidence represents information relevant to a claim.

Fields:

- id
- claim_id
- title
- description
- evidence_type
- direction
- strength
- source_id
- reasoning
- created_at
- updated_at

Direction:

- supports
- challenges
- neutral
- unclear

Strength:

- very_weak
- weak
- moderate
- strong
- very_strong

---

# 4. Sources

Sources identify where information originated.

Fields:

- id
- title
- author
- publisher
- source_type
- url
- publication_date
- credibility_score
- credibility_reasoning
- archived_url
- created_at
- updated_at

A source may be connected to multiple pieces of evidence.

---

# 5. Alternative Explanations

Alternative explanations represent competing interpretations.

Fields:

- id
- topic_id
- title
- description
- supporting_summary
- opposing_summary
- unanswered_questions
- created_at
- updated_at

---

# 6. Categories

Categories organize topics.

Fields:

- id
- name
- description

Possible categories:

- Science
- History
- Politics
- Technology
- Health
- Religion
- Paranormal
- Current Events
- Media
- Other

---

# 7. Tags

Tags provide more detailed classification.

Fields:

- id
- name
- slug

Topics can have multiple tags.

Tags can belong to multiple topics.

This requires a TopicTags relationship.

---

# 8. Users

Fields:

- id
- username
- email
- password_hash
- role
- reputation
- created_at
- updated_at

Possible roles:

- user
- contributor
- moderator
- administrator

Passwords must never be stored as plain text.

---

# 9. User Ratings

Users can record their own assessment of a claim.

Fields:

- id
- user_id
- claim_id
- confidence
- created_at
- updated_at

Possible confidence values:

1 - Very Unlikely
2 - Unlikely
3 - Uncertain
4 - Plausible
5 - Likely
6 - Very Likely

Community opinion must remain separate from Controversion's evidence assessment.

---

# 10. Comments

Fields:

- id
- user_id
- topic_id
- parent_comment_id
- body
- created_at
- updated_at

parent_comment_id allows replies and discussion threads.

---

# 11. Submissions

Users may submit:

- New topics
- Claims
- Evidence
- Sources
- Corrections

Fields:

- id
- user_id
- submission_type
- submitted_data
- status
- reviewer_id
- review_notes
- created_at
- reviewed_at

Possible status:

- pending
- approved
- rejected
- duplicate
- needs_revision

---

# 12. Change History

Important changes should be auditable.

Fields:

- id
- entity_type
- entity_id
- user_id
- action
- previous_value
- new_value
- reason
- created_at

This allows Controversion to show how information and assessments change over time.

---

# 13. Topic Relationships

Topics may be related to other topics.

Fields:

- topic_id
- related_topic_id
- relationship_type

Examples:

- related
- prerequisite
- contradicts
- historical_connection

---

# Core Relationships

Topic
→ Claims
→ Evidence
→ Sources

Topic
→ Alternative Explanations

Topic
→ Tags

Topic
→ Comments

Claim
→ User Ratings

Users
→ Submissions

All important entities
→ Change History

---

# Design Principle

The database should preserve the distinction between:

FACT

CLAIM

EVIDENCE

SOURCE

INTERPRETATION

COMMUNITY OPINION

These should never be treated as interchangeable pieces of information.
