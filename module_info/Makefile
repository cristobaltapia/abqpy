.PHONY: all clean

ABQVERSIONS= abq2017 \
	     abq2018 \
	     abq2020 \
	     abq2020hf17 \
	     abq2021 \
	     abq2021hf14 \
	     abq2022 \
	     abq2022hf4 \
	     abq2023 \

all: $(ABQVERSIONS)

clean:
	rm -f *.rpy.*
	rm -f *.rpy

%:
	$* cae noGUI=extract_module_info.py

