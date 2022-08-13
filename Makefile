CSV		= RespawnTimeDB.csv
PROG	= ./RespawnTimer.py
DB		= RespawnTimeDB
TIMER	= RespawnTimer
GINA	= ShareData.xml

all: clean xml gtp

xml: $(PROG) $(CSV)
	$(PROG)

gtp: $(DB).xml $(TIMER).xml
	cp $(DB).xml $(GINA)
	zip $(DB).gtp $(GINA)
	rm -f $(GINA)
	cp $(TIMER).xml $(GINA)
	zip $(TIMER).gtp $(GINA)
	rm -f $(GINA)

clean:
	rm -f $(DB).xml $(TIMER).xml $(DB).gtp $(TIMER).gtp

