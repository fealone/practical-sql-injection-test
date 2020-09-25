create table if not exists public (name varchar(100));
create table if not exists secure (token varchar(100));
insert into public (name) values (\'hoge\');
insert into public (name) values (\'foo\');
insert into public (name) values (\'fuga\');
insert into secure (token) values (\'c2dbf691-4275-47a5-a392-c64aa7fa3c2d\');
insert into secure (token) values (\'f4d78ea1-ded7-436e-8c89-984b93552d91\');
insert into secure (token) values (\'442744cc-62cb-41a5-b3b4-6bc90d9c5951\');
