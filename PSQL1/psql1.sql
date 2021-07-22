--
-- PostgreSQL database dump
--

-- Dumped from database version 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: lardie
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.actors OWNER TO lardie;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: lardie
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO lardie;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lardie
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: lardie
--

CREATE TABLE public.directors (
    name text
);


ALTER TABLE public.directors OWNER TO lardie;

--
-- Name: films; Type: TABLE; Schema: public; Owner: lardie
--

CREATE TABLE public.films (
    film text
);


ALTER TABLE public.films OWNER TO lardie;

--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: lardie
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: lardie
--

COPY public.actors (id, name) FROM stdin;
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: lardie
--

COPY public.directors (name) FROM stdin;
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: lardie
--

COPY public.films (film) FROM stdin;
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lardie
--

SELECT pg_catalog.setval('public.actors_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

