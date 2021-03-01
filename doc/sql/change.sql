# add column
alter table `learn_plan` add column `title` varchar(50) not null default "" comment "标题" after `id`;