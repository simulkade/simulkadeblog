<!--
.. title: Curriculum vitae
.. slug: cv
.. date: 2015-09-26 18:47:01 UTC+02:00
.. tags: CV
.. category:
.. link:
.. description:
.. type: text
-->


# Curriculum Vitae
## Personal information
**Ali Akbar Eftekhari**

+ *Date and place of birth*: 1981, [Estahban](https://www.google.nl/maps/place/Estahbān,+Fars,+Iran/), [Iran](https://en.wikipedia.org/wiki/Iran)
+ *Marital status*: Married, [two children](/Aida_met_papa.JPG)
---
## Profile
I am a Chemical and Petroleum Engineering graduate with several years of experience in the modeling and simulation of [upstream](https://en.wikipedia.org/wiki/Upstream_%28petroleum_industry%29) and [downstream](https://en.wikipedia.org/wiki/Downstream_%28petroleum_industry%29) oil and gas processes. Besides working with [commercial simulators](https://en.wikipedia.org/wiki/List_of_chemical_process_simulators), I have developed prototype computer tools for the modeling and simulation of multicomponent [phase equilibrium](https://en.wikipedia.org/wiki/Vapor%E2%80%93liquid_equilibrium) and multiphase flow in porous media. During my PhD, I used the concept of [exergy](https://en.wikipedia.org/wiki/Exergy) to devise and develop a procedure for the [life-cycle-assessment](https://en.wikipedia.org/wiki/Life-cycle_assessment) of zero-emission fossil fuel recovery. As a post-doc researcher, I worked on the application of nanotechnology in the enhanced oil recovery. I have designed and conducted experiments in different scales, including production and stabilization of colloidal suspensions to high-pressure/high-temperature core-flooding experiments for [EOR](https://en.wikipedia.org/wiki/Enhanced_oil_recovery). My scientific passion is the [exergy](https://en.wikipedia.org/wiki/Exergy) analysis of the energy conversion processes. My other interest is the investigation of various physical and chemical interactions (fluid-fluid, rock-fluid) in the flow of [multiphase fluids in porous media](https://en.wikipedia.org/wiki/Fluid_flow_through_porous_media). I am also interested in numerical methods and computer programming, fluid phase equilibria, and [process simulation](https://en.wikipedia.org/wiki/Process_simulation) and optimization.

---

## Education
+ **2008-2012** PhD student, *Low emission conversion of fossil fuels with simultaneous or consecutive storage of carbon dioxide*, [Delft University of Technology](http://www.tudelft.nl/en/), Delft, the Netherlands [(Download my thesis)](/mainfile_finalversion.pdf)
+ **2003-2005** M.Sc., Chemical Engineering - Transport Phenomena and Separation Processes, [Sharif University of Technology](https://en.wikipedia.org/wiki/Sharif_University_of_Technology), Tehran, Iran ([Download my thesis](/master_thesis.pdf), in Persian, with English summary), (Me [during](/master_defense.JPG) and [after](/after_master_defense.JPG) defense)
+ **1999-2003** B.Sc., Chemical Engineering - Petrochemical Processes, [Shiraz University](https://en.wikipedia.org/wiki/Shiraz_University), Shiraz, Iran

---

## Teaching experience
### 2005-2008
+ Simulation and optimization of chemical/petrochemical processes using commercial process simulators [(See a presentation here)](/HYSYS_and_Aspen_Plus_Course_Program.ppt)
+ programming and optimization with Matlab.
### 2012-2015
+ Exergy analysis of geothermal energy (MSc course, one session), Delft University of Technology. ([Presentation1](/geothermalenergy_PEmeeting.sozi.html), [Presentation2](/An_Introduction_to_Exergy_Analysis_in_geothermal_energy_v2.pptx), [Handouts](/handouts_extended_v02.pdf))
+ Thermodynamic calculation of the physical properties of multi-component multi-phase mixtures (PhD course), Delft University of Technology. (Matlab/Octave [code1](https://github.com/simulkade/PVTtool/blob/master/Examples/pure_component_density.m), [code2](https://github.com/simulkade/PVTtool/blob/master/Examples/methanol_water_vle.m))

---

## Work experience
### Process Engineer (2005-2008)
+ Experimental study, simulation, and scale-up of a methyl acetate hydrolysis process from bench to pilot scale; *National Iranian Petrochemical Company – Research and Development*.
+ Preliminary design of a pilot scale structured-bed distillation column for research purposes; *National Iranian Petrochemical Company – Research and Development*.
+ Simulation of various petrochemical processes including high impact polystyrene, unsaturated polyester resin, and natural gas processing/crude oil refinery units.
### Post-doc researcher (2012–2015, TU Delft)
+ Conducting more than 50 core flooding experiments.
+ Developing computer codes for the optimization of foam model parameters and numerical simulation of foam flow in porous media.
+ Experimental investigation of nano-particle-stabilized foam flow in porous media.
+ Production of nanoparticles and investigation of the stability of nanoparticle suspensions.
+ Flow of polymer-enhanced foam in porous media.
+ Stability of foam in presence of oil in porous media.
### Post-doc researcher (2016-2017, Technical University of Denmark)
+ Thermodynamic analysis of brine-oil-chalk systems
+ Thermodynamic analysis of the low-grade geothermal energy systems
+ Developing computer programs for modelling and simulation of non-isothermal multicomponent multi-phase reactive flow in porous media (including bio/chemical reactions)
+ Coupling two phase flow of water and oil in chalk reservoirs with geochemical reactions
+ Mathematical modeling of DME-enhanced water flooding in chalk reservoirs

---

## Voluntary activities
### Organizer
+ Interpore (2017): Co-organizing a session on “Modified-salinity-brine flooding: from pore to field scale”, Rotterdam, the Netherlands
+ EAGE (2018): Co-organizing a session on “Modified Salinity Waterflooding in Chalk Reservoirs”, Copenhagen, Denmark
+ Modified-salinity water flooding workshop (June 2018), Technical University of Denmark
### Reviewer
+ Energy
+ Petroleum Science and Engineering
+ Fuel
+ Energy & Fuels

---

## Modeling and simulation experience
+ **Phase equilibrium of CO2-water-salt mixture**: An optimized PRSV equation of state with NRTL-based MHV2 mixing rule, written in Matlab. The code was re-written in C and is being used in a Riemann solver package at IMPA, Brazil.
+ **Finite volume toolbox for transient convection-diffusion equations**: A [Matab](http://www.mathworks.com/products/matlab/)/[Octave](https://www.gnu.org/software/octave/) toolbox, [publicly available](https://github.com/simulkade/FVTool), which can be used to solve linear/nonlinear coupled [convection-diffusion](https://en.wikipedia.org/wiki/Convection%E2%80%93diffusion_equation) equations in 1, 2, and 3D domains; several sophisticated applications already implemented including fully-implicit solver for immiscible displacement, foam flow in porous media, and [density-driven](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93B%C3%A9nard_convection) natural convection. The code is also [available](https://github.com/simulkade/JFVM.jl) as a [Julia](http://julialang.org/) package.
+ **A PVT toolbox for Matlab**: A Matlab/Octave [toolbox](https://github.com/simulkade/PVTtool) for the vapor-liquid flash calculations and stability test, and calculation of thermodynamic and transport properties of multicomponent mixtures. It contains physical and chemical data for
around 500 pure components.
+ **A Julia wrapper for the geochemistry package PHREEQC**: A [julia package](https://github.com/simulkade/JPhreeqc.jl) that calls the C wrapper of [PhreeqcRM](https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/), with some convenience functions for interactive development of reactive-transport solvers

---

## Laboratory experience
[Gas chromatography](https://en.wikipedia.org/wiki/Gas_chromatography) (GC), [Dynamic Light Scattering](http://www.malvern.com/en/products/product-range/zetasizer-range/zetasizer-nano-range/) (zeta potential, particle size distribution), [CT-scanner](http://www.siemensctscanner.com/), core-flooding, high pressure equipments ([Swagelok](https://www.swagelok.com/)), [mass flow controllers](http://www.bronkhorst.com/), [pumps](http://www.chandlereng.com/Products/Quizix%20Precision%20Pumps/index.aspx), pressure and temperature sensors, [data-acquisition](https://en.wikipedia.org/wiki/Data_acquisition) (DAQ).

---

## Supervisory experience
+ **Mohammadreza Mehdizadeh (2017)**, Master thesis, *DME-enhanced water flooding in chalk reservoirs*, DHRTC, Technical University of Denmark
+ **Hubert Karon (2017)**, Master thesis, *Temperature dependency of Smart Water flooding in Chalk*, DHRTC, Technical University of Denmark
+ **Mick Roukema (2015)**, Master thesis. *Polymer-stabilized foam for enhanced oil recovery*, Petroleum Engineering, Delft university of technology
+ **Jaap Regelink (2015)**, Bachelor thesis. *Calculating black-oil parameters for volatile oils*, Petroleum Engineering, Delft university of technology
+ **Joris Roebroeks (2014)**, Master thesis. *Nanoparticle-enhanced foam in carbonate and sandstone reservoirs*, Petroleum Engineering, Delft university of technology ([link](http://repository.tudelft.nl/view/ir/uuid:ed2c4e5b-71c8-476d-833a-b51ea7d8f9e4/))
+ **Jia Wei (2013)**, Master thesis. *Nanoparticle-stabilized foam for enhanced-oil-recovery*, Petroleum Engineering, Delft university of technology
+ **Ioannis Dafnomilis (2012)**, Master thesis, *A workstream for exergy analysis of carbon capture and storage through enhanced oil Recovery*, Sustainable Energy Technology, Delft university of technology
+ **Jonathan De Mooij (2010)**, Master thesis. *Exergy analysis of the use of geothermal energy and carbon capture, transportation and storage in underground aquifers*, Sustainable Energy Technology, Delft university of technology ([link](http://repository.tudelft.nl/view/ir/uuid%3A1af2dec8-542e-4116-af02-fd3f99816358/))

---

## Language skills
+ Persian (native)
+ English (fluent)
+ Dutch (basic)

---

## Computer skills
+ **Operating systems**:
    - [Linux](https://en.wikipedia.org/wiki/Linux)
    - [Microsoft Windows](http://www.microsoft.com/en-us/windows)
+ **Programming languages**:
    - [C++](https://en.wikipedia.org/wiki/C%2B%2BBuilder) ([sample code](/envelope_cbuilder.zip))
    - [Visual Basic](https://en.wikipedia.org/wiki/Visual_Basic) ([sample code](/phaseenvelope_vb.zip))
    - [MATLAB](https://en.wikipedia.org/wiki/MATLAB) ([sample code](https://github.com/simulkade/FVTool))
    - [Python](https://www.python.org/)
    - [Julia](http://julialang.org/) ([sample code](https://github.com/simulkade/JFVM.jl)),
    - [Labview](http://www.ni.com/labview/)
+ **Process simulators** [(See a presentation here)](/HYSYS_and_Aspen_Plus_Course_Program.ppt):
    - [Aspen Plus](http://www.aspentech.com/products/engineering/aspen-plus/)
    - [Aspen Hysys](http://www.aspentech.com/products/aspen-hysys/)
    - [Aspen Polymers](http://www.aspentech.com/products/aspen-polymers-plus.aspx)
    - [Aspen Icarus](http://www.aspentech.com/products/economic-evaluation/aspen-in-plant-cost-estimator/)
    - [Chemcad](http://www.chemstations.com/)
    - [Pro/II](http://software.schneider-electric.com/products/simsci/design/pro-ii/)
+ **Petroleum Engineering**:
    - [Petrel](http://www.software.slb.com/products/platform/Pages/petrel.aspx), [Eclipse](http://www.software.slb.com/products/foundation/Pages/eclipse.aspx)
    - [CMG](http://www.cmgl.ca/home)
+ **Multiphysics**:
    - [COMSOL](https://www.comsol.nl/)

---

## Awards
+ Highest GPA among 78 Chemical Engineering B.Sc. graduates, Shiraz University, Shiraz, Iran, September 2003
+ Highest GPA among 10 M.Sc. graduates of Transport Phenomena and Separation Processes, Sharif University of Technology, Tehran, Iran, September 2005
+ Best paper award, annual research meeting of the Department of Geoscience and Engineering and Remote Sensing, February 2013.
+ Best poster award, DHRTC technology conference, Denmark, November 2016

---

## Publications
For an up to date list, please visit:

+ [Google Scholar profile](https://scholar.google.nl/citations?user=hBKHOIcAAAAJ&hl=en)
+ [ResearchGate profile](https://www.researchgate.net/profile/Ali_Akbar_Eftekhari)
+ [Orcid](http://orcid.org/0000-0001-6856-5858)

Here's a selected list of my publications:

### Refereed journals
1. **Eftekhari, A.A.**, Thomsen, K., Stenby, E. H., & Nick, H. M. (2017). Thermodynamic analysis of chalk-brine-oil interactions. Energy & Fuels. doi: 10.1021/acs.energyfuels.7b02019
2. **Eftekhari, A.A.**, Wolf, K.H.H., Rogut, J. & Bruining, J. (2017), Energy and exergy analysis of alternating injection of oxygen and steam in the low emission underground gasification of deep thin coal. Applied Energy, 208C (2017) pp. 62-71
3. **Eftekhari, A.A.**, & Farajzadeh, R. (2017). Effect of Foam on Liquid Phase Mobility in Porous Media. Scientific Reports. 7, 43870; doi: 10.1038/srep43870.
4. **Eftekhari, A.A.**, Krastev, R., Farajzadeh, R., (2015), Foam Stabilized by Fly-Ash Nanoparticles for Enhancing Oil Recovery, Industrial & Engineering Chemistry Research 54 (50), 12482–12491 [(Download)](https://www.researchgate.net/publication/285711305_Foam_Stabilized_by_Fly-Ash_Nanoparticles_for_Enhancing_Oil_Recovery)
5. **Eftekhari, A.A.**, Wolf, K.H.H., Rogut, J. & Bruining, J. (2015), Mathematical modeling of alternating injection of oxygen and steam in underground coal gasification. *International Journal of Coal Geology*. [(Download)](https://www.researchgate.net/publication/281334363_Mathematical_modeling_of_alternating_injection_of_oxygen_and_steam_in_underground_coal_gasification)
6. Farajzadeh, R., Lotfollahi, M., **Eftekhari, A.A.**, Rossen, W. R., & Hirasaki, G. J. (2015). Effect of permeability on implicit-texture foam-model parameters and the limiting capillary pressure. *Energy & Fuels*. [(Download)](https://www.researchgate.net/publication/275465969_Effect_of_Permeability_on_Implicit-Texture_Foam_Model_Parameters_and_the_Limiting_Capillary_Pressure)
7. **Eftekhari, A.A.**, Van Der Kooi, H., & Bruining, J. (2012). Exergy analysis of underground coal gasification with simultaneous storage of carbon dioxide. *Energy*, 45(1), 729-745. [(Download)](https://www.researchgate.net/publication/236607938_Exergy_analysis_of_underground_coal_gasification_with_simultaneous_storage_of_carbon_dioxide)
8. Battistutta, E., **Eftekhari, A.A.**, Bruining, H., & Wolf, K. H. (2011). Manometric sorption measurements of CO2 on moisture-equilibrated bituminous coal. *Energy & Fuels*, 26(1), 746-752. [(Download)](https://www.researchgate.net/publication/263946989_Manometric_Sorption_Measurements_of_CO2_on_Moisture-Equilibrated_Bituminous_Coal)
9. Ehteshami, M., Rahimi, N., **Eftekhari, A.A.**, & Nasr, M.J. (2006). Kinetic study of catalytic hydrolysis reaction of methyl acetate to acetic acid and methanol. *Iranian Journal of Science & Technology, Transaction B, Engineering*, 30 (B5). [(Download)](https://www.researchgate.net/publication/236607933_Kinetic_study_of_catalytic_hydrolysis_reaction_of_methyl_acetate_to_acetic_acid_and_methanol)
10. Bobbert, F. S. L., Lietaert, K., **Eftekhari, A.A.**, Pouran, B., Ahmadi S. M., Weinans, H., & Zadpoor, A. A. (2017), Additively manufactured metallic porous biomaterials based on minimal surfaces: a unique combination of topological, mechanical, and mass transport properties. Acta Biomaterialia. doi: 10.1016/j.actbio.2017.02.024. 
11. Kapetas, L., Bonnieu, S. V., Farajzadeh, R., **Eftekhari, A.A.**, Shafian, S. M., Bahrim, R. K., & Rossen, W. R. (2017). Effect of permeability on foam-model parameters: an integrated approach from core-flood experiments
through to foam diversion calculations. Colloids and Surfaces A: Physicochemical and Engineering Aspects.
12. Farajzadeh, R., **Eftekhari, A.A.**, Hajibeygi, H., Kahrobaei, S., van der Meer, J. M., Vincent-Bonnieu, S., & Rossen, W. R. (2016). Simulation of Instabilities and Fingering in Surfactant Alternating Gas (SAG) Foam Enhanced Oil Recovery. Journal of Natural Gas Science and Engineering, 34.
13. Zeng, Y., Farajzadeh, R., **Eftekhari, A.A.**, Vincent-Bonnieu, S., Muthuswamy, A., Rossen, W. R., ... & Biswal, S. L. (2016). Role of Gas Type on Foam Transport in Porous Media. Langmuir.
14. Kapetas L, Bonnieu SV, Danelis S, Rossen WR, Farajzadeh R, **Eftekhari A.A.**, Shafian SM, Bahrim RK. (2016). Effect of temperature on foam flow in porous media. Journal of Industrial and Engineering Chemistry. 36:229-37.
15. Zeng, Y., Muthuswamy, A., Ma, K., Wang, L., Farajzadeh, R., Puerto, M., ..., **Eftekhari, A.A.**, & Joyce, J. C. (2016). Insights on Foam Transport from a Texture-Implicit Local-Equilibrium Model with an Improved Parameter Estimation Algorithm. Industrial & Engineering Chemistry Research, 55(28), 7819-7829.

### In proceedings
1. **Eftekhari, A.A.**, M. la Cour Christensen, H. Maghami Nick, K. Thomsen & E. Stenby. (2017). Uncertainties in the Mechanistic Models of the Modified Brine Water-flooding of Chalk. 19th European Symposium on Improved Oil Recovery, Stavanger, Norway
1. **Eftekhari, A.A.** & Farajzadeh, R. (2015). Fly-Ash Nanoparticles for Enhancing Oil Recovery: An Experimental Investigation, *SPE Kuwait Oil & Gas Show and Conference*.
2. Farajzadeh, R., Lotfollahi, M., **Eftekhari, A.A.**, Rossen, W. R., & Hirasaki, G. J. (2015, April). Effect of Permeability on Foam-model Parameters and the Limiting Capillary Pressure. *In IOR 2015-18th European Symposium on Improved Oil Recovery*. [(Download)](https://www.researchgate.net/publication/275465969_Effect_of_Permeability_on_Implicit-Texture_Foam_Model_Parameters_and_the_Limiting_Capillary_Pressure)
3. Kapetas, L., Vincent-Bonnieu, S., Farajzadeh, R., **Eftekhari, A.A.**, Mohd-Shafian, S. R., Bahrim, R. K., & Rossen, W. R. (2015, April). Effect of Permeability on Foam-model parameters-An Integrated Approach from Coreflood Experiments through to Foam Diversion Calculations. *In IOR 2015-18th European Symposium on Improved Oil Recovery*.
4. Kapetas, L., Vincent Bonnieu, S., Danelis, S., Rossen, W. R., Farajzadeh, R., **Eftekhari, A.A.**, ... & Kamarul Bahrim, R. Z. (2015, March). Effect of temperature on foam flow in porous media. *In SPE Middle East Oil & Gas Show and Conference. Society of Petroleum Engineers*. [(Download)](https://www.researchgate.net/publication/273368072_Effect_of_Temperature_on_Foam_Flow_in_Porous_Media)
5. Farajzadeh, R., **Eftekhari, A.A.**, Hajibeygi, H., van der Meer, J. M., Vincent-Bonnieu, S., & Rossen, W. R. (2015, February). Simulation of Instabilities and Fingering in Surfactant Alternating Gas (SAG) Foam Enhanced Oil Recovery. *In SPE Reservoir Simulation Symposium. Society of Petroleum Engineers*.
6. Roebroeks, J., **Eftekhari, A.A.**, Farajzadeh, R., & Vincent-Bonnieu, S. (2015, April). Nanoparticle Stabilized Foam in Carbonate and Sandstone Reservoirs. *In IOR 2015-18th European Symposium on Improved Oil Recovery*. [(Download)](https://www.researchgate.net/publication/275465912_Nanoparticle_Stabilized_Foam_in_Carbonate_and_Sandstone_Reservoirs)
7. Khosrokhavar, R., **Eftekhari, A.A.**, Farajzdadeh, R., Wolf, K. H., & Bruining, H. (2015, April). Effect of Salinity and Pressure on the Rate of Mass Transfer in Aquifer Storage of CO2. *In IOR 2015-18th European Symposium on Improved Oil Recovery*. [(Download)]()
8. **Eftekhari, A.A.**, Bruining, J., Wahanik, H., & Marchesin, D. (2011, January). CO2 injection in the sub-salt water layers at 7000 m depth. *In SPE Reservoir Simulation Symposium. Society of Petroleum Engineers*. [(Download)](https://www.researchgate.net/publication/236607930_CO2_injection_in_sub-salt_water_layers_at_7000m_depth)
9. **Eftekhari, A.A.**, Heimovaara, T.J., & Bruining, J. (2010, January). A case study of electricity generation from low quality geothermal energy sources. *In First International Conference on Frontiers in Shallow Subsurface Technology*. [(Download)](https://www.researchgate.net/publication/236607931_A_case_study_of_electricity_generation_from_low_quality_geothermal_energy_sources)
10. Heimovaara, T., **Eftekhari, A.A.**, & Bruining, H. (2010, January). Quantification of sustainability of soil remediation, the exergy concept. *In First International Conference on Frontiers in Shallow Subsurface Technology*. [(Download)](https://www.researchgate.net/publication/236607932_Quantification_of_sustainability_of_soil_remediation_the_exergy_concept)
11. Wahanik, H., **Eftekhari, A.A.**, Bruining, J., Marchesin, D., & Wolf, K.H.A. (2010, January). Analytical solutions for mixed CO2-water injection in geothermal reservoirs. *In Canadian Unconventional Resources and International Petroleum Conference. Society of Petroleum Engineers*. [(Download)](https://www.researchgate.net/publication/236607937_Analytical_Solutions_for_Mixed_CO2-Water_Injection_in_Geothermal_Reservoirs)
### Technical reports
1. **Eftekhari, A.A.** (2014). Nanoparticle-stabilized foam: An experimental investigation of nanoparticle production, suspension stability, foaminess, and foam strength. *Submitted to Shell Intl. E&P BV, Rijswijk, the Netherlands*.
2. **Eftekhari, A.A.** (2013). Low Emission Conversion of Fossil Fuels with Simultaneous or Consecutive Storage of Carbon Dioxide. PhD thesis, *Delft University of Technology*.
3. **Eftekhari, A.A.** (2012). Underground coal gasification with a low carbon content product: a literature review. *Submitted to TNO, Utrecht, the Netherlands*.
### Conference abstracts
1. **Eftekhari, A.A.**, Farajzadeh, R. & Bruining, J. (2011, March). Experimental investigation of enhanced CO2 mass transfer in water-saturated porous media. *3rd Interpore Conference, Bordeaux*. [(Download poster)](/Interpore_bordeaux_poster_2011.pdf)
2. **Eftekhari, A.A.** & Bruining, J. (2010). Exergy analysis of underground coal gasification with simultaneous storage of carbon dioxide. *8th European coal conference – Darmstadt*. [(Download presentation)](/Eftekhari_Darmstadt final.pptx)
3. **Eftekhari, A.A.**, Bruining, J., Rogut, J. & Van Batenburg, D.W. (2010). Cyclic production of CO2-rich and hydrogen-rich gas in underground coal gasification. *8th European coal conference – Darmstadt*. [(Download poster)](/Darmsdadt_Poster.pdf)
4. **Eftekhari, A.A.** & Wahanik, H. (October 2009). The Riemann solution for the injection of supercritical carbon dioxide and vapor in porous media. *International Conference on Non-linearities and Upscaling in Porous Media, Stuttgart, Germany*. ([Poster](/StturgartPosterVersionfinal5Ehsan-Helmut.pdf), shortlisted for the best poster award)
### Technical group meetings
1. **Eftekhari, A.A.** (2012). Experimental investigation of enhanced CO2 mass transfer in water-saturated porous media, *Interpore-Shell meeting, Shell, Rijswijk, the Netherlands*. ([Poster](/interporeshell2.pdf))
2. **Eftekhari, A.A.** (March 2011). experimental validation of natural convection in aquifer storage of CO2. *NUPUS meeting, Freudenstadt, Germany* ([Presentation](/NUPUSpresentation04.svg))
3. **Eftekhari, A.A.** (January 2010). Theoretical, practical, and sustainable exergetic recovery of energy resources. *Annual research meeting, Department of Geotechnology, Delft University of Technology*. ([Poster](/Posterdelft2010final.pdf))
4. **Eftekhari, A.A.** (2009). Cyclic production of carbon dioxide-rich and hydrogen-rich gas in Underground coal gasification. *Geo-engineering lecture series, Delft University of Technology*. ([Presentation](/channelgasify.svg))
5. **Eftekhari, A.A.** (2008). An introduction to exergy analysis. *Geo-engineering lecture series, Delft University of Technology*. ([Presentation](/An_Introduction_to_Exergy_Analysisb.pdf))
6. **Eftekhari, A.A.** (March 2008). Physical and chemical equilibrium of CO2-Water-Mineral system using Aspen Plus process simulator. *NUPUS meeting, Freudenstadt, Germany*. ([Presentation](/first_presentation_nupus.ppt))
