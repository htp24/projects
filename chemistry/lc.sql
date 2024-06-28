CREATE TABLE lc_submission (
      lc_num INTEGER NOT NULL,
  student_id TEXT NOT NULL,
          q1 TEXT,
          q2 TEXT,
          q3 TEXT,
          q4 TEXT,
          q5 TEXT,
          q6 TEXT,
          q7 TEXT,
          q8 TEXT,
          q9 TEXT,
         q10 TEXT,
         q11 TEXT,
         q12 TEXT,
         q13 TEXT,
         q14 TEXT,
         q15 TEXT,
         q16 TEXT,
         q17 TEXT,
         q18 TEXT,
         q19 TEXT,
         q20 TEXT
);

-- maybe no need?
CREATE TABLE lc_answers (
      lc_num INTEGER NOT NULL,
          q1 TEXT,
          q2 TEXT,
          q3 TEXT,
          q4 TEXT,
          q5 TEXT,
          q6 TEXT,
          q7 TEXT,
          q8 TEXT,
          q9 TEXT,
         q10 TEXT,
         q11 TEXT,
         q12 TEXT,
         q13 TEXT,
         q14 TEXT,
         q15 TEXT,
         q16 TEXT,
         q17 TEXT,
         q18 TEXT,
         q19 TEXT,
         q20 TEXT,
);

CREATE TABLE lc_scores (
      lc_num INTEGER NOT NULL,
  student_id TEXT NOT NULL,
       score NUMERIC
);
