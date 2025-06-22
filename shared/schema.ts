import { pgTable, serial, text, integer, boolean, timestamp, varchar, numeric } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

// Users table
export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  username: varchar('username', { length: 64 }).notNull().unique(),
  fullName: varchar('full_name', { length: 100 }),
  email: varchar('email', { length: 100 }),
  phone: varchar('phone', { length: 20 }),
  passwordHash: varchar('password_hash', { length: 256 }).notNull(),
  role: varchar('role', { length: 20 }).notNull().default('student'),
  points: integer('points').default(0),
  resetToken: varchar('reset_token', { length: 100 }),
  resetTokenExpiry: timestamp('reset_token_expiry'),
  createdAt: timestamp('created_at').defaultNow(),
});

// Videos table
export const videos = pgTable('videos', {
  id: serial('id').primaryKey(),
  title: varchar('title', { length: 100 }).notNull(),
  url: varchar('url', { length: 200 }),
  filePath: varchar('file_path', { length: 200 }),
  description: text('description'),
  uploadedBy: integer('uploaded_by').references(() => users.id).notNull(),
  createdAt: timestamp('created_at').defaultNow(),
  requiresCode: boolean('requires_code').default(true),
  pointsCost: integer('points_cost').default(0),
  lessonNumber: integer('lesson_number').default(1),
  section: varchar('section', { length: 50 }).default('sec1'),
  isFeatured: boolean('is_featured').default(false),
  videoOrder: integer('video_order').default(0),
  thumbnailUrl: varchar('thumbnail_url', { length: 200 }),
  duration: varchar('duration', { length: 20 }),
  tags: varchar('tags', { length: 200 }),
});

// Tests table
export const tests = pgTable('tests', {
  id: serial('id').primaryKey(),
  title: varchar('title', { length: 200 }).notNull(),
  description: text('description'),
  passingScore: integer('passing_score').default(60),
  timeLimit: integer('time_limit').default(30),
  isPublished: boolean('is_published').default(false),
  createdBy: integer('created_by').references(() => users.id).notNull(),
  createdAt: timestamp('created_at').defaultNow(),
  maxAttempts: integer('max_attempts').default(3),
});

// Test questions table
export const testQuestions = pgTable('test_questions', {
  id: serial('id').primaryKey(),
  testId: integer('test_id').references(() => tests.id).notNull(),
  questionText: text('question_text').notNull(),
  questionType: varchar('question_type', { length: 20 }).notNull().default('multiple_choice'),
  points: integer('points').default(1),
  imageUrl: varchar('image_url', { length: 500 }),
  questionOrder: integer('question_order').default(0),
});

// Question choices table
export const questionChoices = pgTable('question_choices', {
  id: serial('id').primaryKey(),
  questionId: integer('question_id').references(() => testQuestions.id).notNull(),
  choiceText: text('choice_text').notNull(),
  isCorrect: boolean('is_correct').default(false),
  choiceOrder: integer('choice_order').default(0),
});

// Test attempts table
export const testAttempts = pgTable('test_attempts', {
  id: serial('id').primaryKey(),
  testId: integer('test_id').references(() => tests.id).notNull(),
  userId: integer('user_id').references(() => users.id).notNull(),
  score: numeric('score', { precision: 5, scale: 2 }).default('0'),
  passed: boolean('passed').default(false),
  startedAt: timestamp('started_at').defaultNow(),
  submittedAt: timestamp('submitted_at'),
  timeSpent: integer('time_spent').default(0),
});

// Test answers table
export const testAnswers = pgTable('test_answers', {
  id: serial('id').primaryKey(),
  attemptId: integer('attempt_id').references(() => testAttempts.id).notNull(),
  questionId: integer('question_id').references(() => testQuestions.id).notNull(),
  choiceId: integer('choice_id').references(() => questionChoices.id),
  textAnswer: text('text_answer'),
  isCorrect: boolean('is_correct').default(false),
});

// Comments table
export const comments = pgTable('comments', {
  id: serial('id').primaryKey(),
  videoId: integer('video_id').references(() => videos.id).notNull(),
  userId: integer('user_id').references(() => users.id).notNull(),
  commentText: text('comment_text').notNull(),
  createdAt: timestamp('created_at').defaultNow(),
});

// Video views table
export const videoViews = pgTable('video_views', {
  id: serial('id').primaryKey(),
  videoId: integer('video_id').references(() => videos.id).notNull(),
  userId: integer('user_id').references(() => users.id).notNull(),
  viewedAt: timestamp('viewed_at').defaultNow(),
});

// Lecture codes table
export const lectureCodes = pgTable('lecture_codes', {
  id: serial('id').primaryKey(),
  videoId: integer('video_id').references(() => videos.id).notNull(),
  code: varchar('code', { length: 20 }).notNull().unique(),
  createdAt: timestamp('created_at').defaultNow(),
  isActive: boolean('is_active').default(true),
  assignedTo: integer('assigned_to').references(() => users.id),
  isUsed: boolean('is_used').default(false),
});

// Announcements table
export const announcements = pgTable('announcements', {
  id: serial('id').primaryKey(),
  title: varchar('title', { length: 200 }).notNull(),
  content: text('content').notNull(),
  createdBy: integer('created_by').references(() => users.id).notNull(),
  createdAt: timestamp('created_at').defaultNow(),
  isPublished: boolean('is_published').default(true),
  priority: varchar('priority', { length: 20 }).default('normal'),
});

// Relations
export const usersRelations = relations(users, ({ many }) => ({
  videos: many(videos),
  comments: many(comments),
  videoViews: many(videoViews),
  testAttempts: many(testAttempts),
  createdTests: many(tests),
  announcements: many(announcements),
}));

export const videosRelations = relations(videos, ({ one, many }) => ({
  uploader: one(users, {
    fields: [videos.uploadedBy],
    references: [users.id],
  }),
  comments: many(comments),
  views: many(videoViews),
  lectureCodes: many(lectureCodes),
}));

export const testsRelations = relations(tests, ({ one, many }) => ({
  creator: one(users, {
    fields: [tests.createdBy],
    references: [users.id],
  }),
  questions: many(testQuestions),
  attempts: many(testAttempts),
}));

export const testQuestionsRelations = relations(testQuestions, ({ one, many }) => ({
  test: one(tests, {
    fields: [testQuestions.testId],
    references: [tests.id],
  }),
  choices: many(questionChoices),
  answers: many(testAnswers),
}));

export const questionChoicesRelations = relations(questionChoices, ({ one, many }) => ({
  question: one(testQuestions, {
    fields: [questionChoices.questionId],
    references: [testQuestions.id],
  }),
  answers: many(testAnswers),
}));

export const testAttemptsRelations = relations(testAttempts, ({ one, many }) => ({
  test: one(tests, {
    fields: [testAttempts.testId],
    references: [tests.id],
  }),
  user: one(users, {
    fields: [testAttempts.userId],
    references: [users.id],
  }),
  answers: many(testAnswers),
}));

export const testAnswersRelations = relations(testAnswers, ({ one }) => ({
  attempt: one(testAttempts, {
    fields: [testAnswers.attemptId],
    references: [testAttempts.id],
  }),
  question: one(testQuestions, {
    fields: [testAnswers.questionId],
    references: [testQuestions.id],
  }),
  choice: one(questionChoices, {
    fields: [testAnswers.choiceId],
    references: [questionChoices.id],
  }),
}));

export const commentsRelations = relations(comments, ({ one }) => ({
  video: one(videos, {
    fields: [comments.videoId],
    references: [videos.id],
  }),
  author: one(users, {
    fields: [comments.userId],
    references: [users.id],
  }),
}));

export const videoViewsRelations = relations(videoViews, ({ one }) => ({
  video: one(videos, {
    fields: [videoViews.videoId],
    references: [videos.id],
  }),
  viewer: one(users, {
    fields: [videoViews.userId],
    references: [users.id],
  }),
}));

export const lectureCodesRelations = relations(lectureCodes, ({ one }) => ({
  video: one(videos, {
    fields: [lectureCodes.videoId],
    references: [videos.id],
  }),
  assignedUser: one(users, {
    fields: [lectureCodes.assignedTo],
    references: [users.id],
  }),
}));

export const announcementsRelations = relations(announcements, ({ one }) => ({
  creator: one(users, {
    fields: [announcements.createdBy],
    references: [users.id],
  }),
}));