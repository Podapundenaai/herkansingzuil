CREATE TABLE Bericht(
      bericht_id SERIAL,
      moderator_id SERIAL,
      tekst   varchar(140),
      datum  date,
      tijd time,
      PRIMARY KEY(bericht_id),
      FOREIGN KEY(moderator_id) REFERENCES Moderator(moderator_id),
    );

CREATE TABLE Moderator(
      moderator_id SERIAL,
      datum date,
      tijd  time,
      naam varchar(255),
      email varchar(255),
      PRIMARY KEY(moderator_id)
    );
CREATE TABLE station_service (
     station_city VARCHAR (50) PRIMARY KEY NOT NULL,
     country VARCHAR (2) NOT NULL,
     ov_bike BOOLEAN NOT NULL,
     elevator BOOLEAN NOT NULL,
     toilet BOOLEAN NOT NULL,
     park_and_ride BOOLEAN NOT NULL
);
