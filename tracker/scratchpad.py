/Users/wright.j/django-test/bin/python /Applications/PyCharm.app/Contents/helpers/pydev/pydevconsole.py 50672 50673
import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend(['/Users/wright.j/PycharmProjects/OSD', '/Applications/PyCharm.app/Contents/helpers/pycharm', '/Applications/PyCharm.app/Contents/helpers/pydev'])
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run("/Users/wright.j/PycharmProjects/OSD")
PyDev console: starting.
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Django 2.0.1
from tracker.models import *
Sitting.objects.all()
<QuerySet [<Sitting: Y10 End of Year MCQ 10C/Ph1>, <Sitting: Y10 End of Year MCQ TEST>, <Sitting: Y10 End of Year MCQ TEST2>, <Sitting: Y10 End of Year Structured TEST>, <Sitting: Y10 End of Year Structured 10C/Ph1>, <Sitting: New test exam TEST>, <Sitting: New test exam TEST>]>
sitting = Sitting.objects.get(pk=6)
sitting
<Sitting: New test exam TEST>
sitting.exam
<Exam: New test exam>
exam = sitting.exam
exam.question_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x10e7538d0>
exam.question_set.all()
<QuerySet []>
from journal import *
from  journal.models import *
entries = StudentJournalEntry.objects.all()
for entry in entires:
    print(entry.student, " ", entry.syllabus_point, ":", entry.syllabus_sub_topic)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'entires' is not defined
for entry in entries:
    print(entry.student, " ", entry.syllabus_point, ":", entry.syllabus_sub_topic)
Daryl TAN   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Daryl TAN   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Daryl TAN   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Daryl TAN   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Daryl TAN   Motion and Measurement 1.2.1 Define speed : None
Daryl TAN   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Daryl TAN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Daryl TAN   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Daryl TAN   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Daryl TAN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Daryl TAN   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Daryl TAN   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Daryl TAN   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Daryl TAN   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Daryl TAN   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Daryl TAN   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Daryl TAN   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Daryl TAN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Daryl TAN   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Daryl TAN   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Daryl TAN   Forces 1.3.3 State that weight is a gravitational force : None
Daryl TAN   Forces 1.3.4 Recall and use the equation W = mg : None
Daryl TAN   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Daryl TAN   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Daryl TAN   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Daryl TAN   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Daryl TAN   Forces 1.4.4 Predict whether an object will float based on density data : None
Daryl TAN   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Daryl TAN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Daryl TAN   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Daryl TAN   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Daryl TAN   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Daryl TAN   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Daryl TAN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Daryl TAN   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Daryl TAN   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Daryl TAN   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Daryl TAN   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Daryl TAN   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Daryl TAN   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Daryl TAN   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Daryl TAN   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Daryl TAN   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Daryl TAN   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Daryl TAN   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Daryl TAN   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Daryl TAN   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Daryl TAN   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Daryl TAN   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Daryl TAN   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Daryl TAN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Daryl TAN   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Daryl TAN   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Daryl TAN   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Daryl TAN   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Daryl TAN   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Daryl TAN   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Daryl TAN   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Daryl TAN   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Daryl TAN   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Daryl TAN   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Daryl TAN   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Daryl TAN   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Daryl TAN   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Daryl TAN   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Daryl TAN   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Daryl TAN   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Daryl TAN   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Daryl TAN   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Daryl TAN   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Daryl TAN   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Daryl TAN   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Daryl TAN   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Daryl TAN   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Daryl TAN   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Daryl TAN   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Daryl TAN   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Daryl TAN   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Daryl TAN   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Daryl TAN   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Daryl TAN   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Daryl TAN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Daryl TAN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Daryl TAN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Daryl TAN   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Daryl TAN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Daryl TAN   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Daryl TAN   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Daryl TAN   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Daryl TAN   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Daryl TAN   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Daryl TAN   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Daryl TAN   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Daryl TAN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Daryl TAN   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Daryl TAN   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Daryl TAN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Daryl TAN   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Daryl TAN   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Daryl TAN   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Daryl TAN   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Daryl TAN   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Daryl TAN   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Daryl TAN   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Daryl TAN   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Daryl TAN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Daryl TAN   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Daryl TAN   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Daryl TAN   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Daryl TAN   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Daryl TAN   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Daryl TAN   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Daryl TAN   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Daryl TAN   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Daryl TAN   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Daryl TAN   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Daryl TAN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Daryl TAN   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Daryl TAN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Daryl TAN   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Daryl TAN   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Daryl TAN   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Daryl TAN   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Daryl TAN   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Daryl TAN   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Daryl TAN   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Daryl TAN   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Daryl TAN   Electricity 4.2.1.1 State that there are positive and negative charges : None
Daryl TAN   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Daryl TAN   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Daryl TAN   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Daryl TAN   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Daryl TAN   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Daryl TAN   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Daryl TAN   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Daryl TAN   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Daryl TAN   Electricity 4.2.1.10 Give an account of charging by induction : None
Daryl TAN   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Daryl TAN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Daryl TAN   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Daryl TAN   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Daryl TAN   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Daryl TAN   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Daryl TAN   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Daryl TAN   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Daryl TAN   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Daryl TAN   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Daryl TAN   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Daryl TAN   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Daryl TAN   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Daryl TAN   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Daryl TAN   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Daryl TAN   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Daryl TAN   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Daryl TAN   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Daryl TAN   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Daryl TAN   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Daryl TAN   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Daryl TAN   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Daryl TAN   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Daryl TAN   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Daryl TAN   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Daryl TAN   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Daryl TAN   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Daryl TAN   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Daryl TAN   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Daryl TAN   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Daryl TAN   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Daryl TAN   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Daryl TAN   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Daryl TAN   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Daryl TAN   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Daryl TAN   Electricity 4.5.2 State that a fuse protects a circuit : None
Daryl TAN   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Daryl TAN   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Brycen IVEC   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Brycen IVEC   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Brycen IVEC   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Brycen IVEC   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Brycen IVEC   Motion and Measurement 1.2.1 Define speed : None
Brycen IVEC   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Brycen IVEC   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Brycen IVEC   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Brycen IVEC   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Brycen IVEC   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Brycen IVEC   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Brycen IVEC   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Brycen IVEC   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Brycen IVEC   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Brycen IVEC   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Brycen IVEC   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Brycen IVEC   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Brycen IVEC   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Brycen IVEC   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Brycen IVEC   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Brycen IVEC   Forces 1.3.3 State that weight is a gravitational force : None
Brycen IVEC   Forces 1.3.4 Recall and use the equation W = mg : None
Brycen IVEC   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Brycen IVEC   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Brycen IVEC   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Brycen IVEC   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Brycen IVEC   Forces 1.4.4 Predict whether an object will float based on density data : None
Brycen IVEC   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Brycen IVEC   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Brycen IVEC   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Brycen IVEC   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Brycen IVEC   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Brycen IVEC   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Brycen IVEC   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Brycen IVEC   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Brycen IVEC   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Brycen IVEC   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Brycen IVEC   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Brycen IVEC   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Brycen IVEC   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Brycen IVEC   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Brycen IVEC   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Brycen IVEC   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Brycen IVEC   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Brycen IVEC   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Brycen IVEC   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Brycen IVEC   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Brycen IVEC   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Brycen IVEC   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Brycen IVEC   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Brycen IVEC   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Brycen IVEC   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Brycen IVEC   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Brycen IVEC   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Brycen IVEC   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Brycen IVEC   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Brycen IVEC   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Brycen IVEC   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Brycen IVEC   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Brycen IVEC   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Brycen IVEC   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Brycen IVEC   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Brycen IVEC   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Brycen IVEC   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Brycen IVEC   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Brycen IVEC   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Brycen IVEC   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Brycen IVEC   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Brycen IVEC   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Brycen IVEC   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Brycen IVEC   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Brycen IVEC   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Brycen IVEC   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Brycen IVEC   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Brycen IVEC   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Brycen IVEC   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Brycen IVEC   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Brycen IVEC   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Brycen IVEC   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Brycen IVEC   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Brycen IVEC   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Brycen IVEC   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Brycen IVEC   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Brycen IVEC   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Brycen IVEC   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Brycen IVEC   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Brycen IVEC   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Brycen IVEC   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Brycen IVEC   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Brycen IVEC   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Brycen IVEC   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Brycen IVEC   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Brycen IVEC   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Brycen IVEC   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Brycen IVEC   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Brycen IVEC   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Brycen IVEC   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Brycen IVEC   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Brycen IVEC   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Brycen IVEC   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Brycen IVEC   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Brycen IVEC   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Brycen IVEC   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Brycen IVEC   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Brycen IVEC   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Brycen IVEC   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Brycen IVEC   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Brycen IVEC   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Brycen IVEC   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Brycen IVEC   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Brycen IVEC   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Brycen IVEC   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Brycen IVEC   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Brycen IVEC   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Brycen IVEC   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Brycen IVEC   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Brycen IVEC   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Brycen IVEC   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Brycen IVEC   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Brycen IVEC   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Brycen IVEC   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Brycen IVEC   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Brycen IVEC   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Brycen IVEC   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Brycen IVEC   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Brycen IVEC   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Brycen IVEC   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Brycen IVEC   Electricity 4.2.1.1 State that there are positive and negative charges : None
Brycen IVEC   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Brycen IVEC   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Brycen IVEC   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Brycen IVEC   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Brycen IVEC   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Brycen IVEC   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Brycen IVEC   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Brycen IVEC   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Brycen IVEC   Electricity 4.2.1.10 Give an account of charging by induction : None
Brycen IVEC   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Brycen IVEC   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Brycen IVEC   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Brycen IVEC   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Brycen IVEC   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Brycen IVEC   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Brycen IVEC   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Brycen IVEC   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Brycen IVEC   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Brycen IVEC   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Brycen IVEC   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Brycen IVEC   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Brycen IVEC   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Brycen IVEC   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Brycen IVEC   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Brycen IVEC   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Brycen IVEC   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Brycen IVEC   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Brycen IVEC   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Brycen IVEC   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Brycen IVEC   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Brycen IVEC   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Brycen IVEC   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Brycen IVEC   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Brycen IVEC   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Brycen IVEC   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Brycen IVEC   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Brycen IVEC   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Brycen IVEC   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Brycen IVEC   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Brycen IVEC   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Brycen IVEC   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Brycen IVEC   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Brycen IVEC   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Brycen IVEC   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Brycen IVEC   Electricity 4.5.2 State that a fuse protects a circuit : None
Brycen IVEC   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Brycen IVEC   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Gary BROWN   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Gary BROWN   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Gary BROWN   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Gary BROWN   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Gary BROWN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Gary BROWN   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Gary BROWN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Gary BROWN   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Gary BROWN   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Gary BROWN   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Gary BROWN   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Gary BROWN   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Gary BROWN   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Gary BROWN   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Gary BROWN   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Gary BROWN   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Gary BROWN   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Gary BROWN   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Gary BROWN   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Gary BROWN   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Gary BROWN   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Gary BROWN   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Gary BROWN   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Gary BROWN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Gary BROWN   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Gary BROWN   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Gary BROWN   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Gary BROWN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Gary BROWN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Gary BROWN   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Gary BROWN   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Gary BROWN   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Gary BROWN   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Gary BROWN   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Gary BROWN   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Gary BROWN   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Gary BROWN   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Gail CHIN   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Gail CHIN   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Gail CHIN   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Gail CHIN   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Gail CHIN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Gail CHIN   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Gail CHIN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Gail CHIN   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Gail CHIN   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Gail CHIN   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Gail CHIN   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Gail CHIN   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Gail CHIN   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Gail CHIN   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Gail CHIN   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Gail CHIN   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Gail CHIN   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Gail CHIN   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Gail CHIN   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Gail CHIN   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Gail CHIN   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Gail CHIN   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Gail CHIN   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Gail CHIN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Gail CHIN   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Gail CHIN   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Gail CHIN   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Gail CHIN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Gail CHIN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Gail CHIN   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Gail CHIN   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Gail CHIN   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Gail CHIN   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Gail CHIN   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Gail CHIN   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Gail CHIN   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Gail CHIN   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Rafael ITO   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Rafael ITO   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Rafael ITO   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Rafael ITO   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Rafael ITO   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Rafael ITO   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Rafael ITO   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Rafael ITO   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Rafael ITO   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Rafael ITO   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Rafael ITO   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Rafael ITO   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Rafael ITO   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Rafael ITO   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Rafael ITO   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Rafael ITO   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Rafael ITO   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Rafael ITO   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Rafael ITO   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Rafael ITO   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Rafael ITO   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Rafael ITO   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Rafael ITO   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Rafael ITO   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Rafael ITO   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Rafael ITO   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Rafael ITO   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Rafael ITO   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Rafael ITO   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Rafael ITO   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Rafael ITO   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Rafael ITO   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Rafael ITO   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Rafael ITO   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Rafael ITO   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Rafael ITO   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Rafael ITO   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Marie AAMANN   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Marie AAMANN   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Marie AAMANN   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Marie AAMANN   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Marie AAMANN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Marie AAMANN   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Marie AAMANN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Marie AAMANN   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Marie AAMANN   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Marie AAMANN   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Marie AAMANN   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Marie AAMANN   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Marie AAMANN   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Marie AAMANN   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Marie AAMANN   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Marie AAMANN   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Marie AAMANN   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Marie AAMANN   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Marie AAMANN   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Marie AAMANN   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Marie AAMANN   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Marie AAMANN   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Marie AAMANN   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Marie AAMANN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Marie AAMANN   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Marie AAMANN   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Marie AAMANN   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Marie AAMANN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Marie AAMANN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Marie AAMANN   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Marie AAMANN   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Marie AAMANN   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Marie AAMANN   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Marie AAMANN   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Marie AAMANN   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Marie AAMANN   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Marie AAMANN   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Marie AAMANN   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Marie AAMANN   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Marie AAMANN   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Marie AAMANN   Motion and Measurement 1.2.1 Define speed : None
Marie AAMANN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Marie AAMANN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Marie AAMANN   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Marie AAMANN   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Marie AAMANN   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Marie AAMANN   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Marie AAMANN   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Marie AAMANN   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Marie AAMANN   Forces 1.3.3 State that weight is a gravitational force : None
Marie AAMANN   Forces 1.3.4 Recall and use the equation W = mg : None
Marie AAMANN   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Marie AAMANN   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Marie AAMANN   Forces 1.4.4 Predict whether an object will float based on density data : None
Marie AAMANN   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Marie AAMANN   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Marie AAMANN   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Marie AAMANN   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Marie AAMANN   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Marie AAMANN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Marie AAMANN   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Marie AAMANN   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Marie AAMANN   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Marie AAMANN   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Marie AAMANN   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Marie AAMANN   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Marie AAMANN   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Marie AAMANN   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Marie AAMANN   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Marie AAMANN   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Marie AAMANN   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Marie AAMANN   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Marie AAMANN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Marie AAMANN   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Marie AAMANN   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Marie AAMANN   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Marie AAMANN   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Marie AAMANN   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Marie AAMANN   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Marie AAMANN   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Marie AAMANN   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Marie AAMANN   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Marie AAMANN   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Marie AAMANN   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Marie AAMANN   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Marie AAMANN   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Marie AAMANN   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Marie AAMANN   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Marie AAMANN   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Marie AAMANN   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Marie AAMANN   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Marie AAMANN   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Marie AAMANN   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Marie AAMANN   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Marie AAMANN   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Marie AAMANN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Marie AAMANN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Marie AAMANN   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Marie AAMANN   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Marie AAMANN   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Marie AAMANN   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Marie AAMANN   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Marie AAMANN   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Marie AAMANN   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Marie AAMANN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Marie AAMANN   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Marie AAMANN   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Marie AAMANN   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Marie AAMANN   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Marie AAMANN   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Marie AAMANN   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Marie AAMANN   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Marie AAMANN   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Marie AAMANN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Marie AAMANN   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Marie AAMANN   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Marie AAMANN   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Marie AAMANN   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Marie AAMANN   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Marie AAMANN   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Marie AAMANN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Marie AAMANN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Marie AAMANN   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Marie AAMANN   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Marie AAMANN   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Marie AAMANN   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Marie AAMANN   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Marie AAMANN   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Marie AAMANN   Electricity 4.2.1.1 State that there are positive and negative charges : None
Marie AAMANN   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Marie AAMANN   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Marie AAMANN   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Marie AAMANN   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Marie AAMANN   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Marie AAMANN   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Marie AAMANN   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Marie AAMANN   Electricity 4.2.1.10 Give an account of charging by induction : None
Marie AAMANN   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Marie AAMANN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Marie AAMANN   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Marie AAMANN   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Marie AAMANN   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Marie AAMANN   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Marie AAMANN   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Marie AAMANN   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Marie AAMANN   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Marie AAMANN   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Marie AAMANN   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Marie AAMANN   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Marie AAMANN   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Marie AAMANN   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Marie AAMANN   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Marie AAMANN   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Marie AAMANN   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Marie AAMANN   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Marie AAMANN   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Marie AAMANN   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Marie AAMANN   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Marie AAMANN   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Marie AAMANN   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Marie AAMANN   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Marie AAMANN   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Marie AAMANN   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Marie AAMANN   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Marie AAMANN   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Marie AAMANN   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Marie AAMANN   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Marie AAMANN   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Marie AAMANN   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Marie AAMANN   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Marie AAMANN   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Marie AAMANN   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Marie AAMANN   Electricity 4.5.2 State that a fuse protects a circuit : None
Marie AAMANN   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Marie AAMANN   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Test Student   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Test Student   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Test Student   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Test Student   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Test Student   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Test Student   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Test Student   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Test Student   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Test Student   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Test Student   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Test Student   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Test Student   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Test Student   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Test Student   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Test Student   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Test Student   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Test Student   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Test Student   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Test Student   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Test Student   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Test Student   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Test Student   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Test Student   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Test Student   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Test Student   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Test Student   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Test Student   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Test Student   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Test Student   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Test Student   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Test Student   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Test Student   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Test Student   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Test Student   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Test Student   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Test Student   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Test Student   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Test Student   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Test Student   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Test Student   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Test Student   Motion and Measurement 1.2.1 Define speed : None
Test Student   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Test Student   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Test Student   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Test Student   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Test Student   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Test Student   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Test Student   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Test Student   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Test Student   Forces 1.3.3 State that weight is a gravitational force : None
Test Student   Forces 1.3.4 Recall and use the equation W = mg : None
Test Student   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Test Student   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Test Student   Forces 1.4.4 Predict whether an object will float based on density data : None
Test Student   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Test Student   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Test Student   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Test Student   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Test Student   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Test Student   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Test Student   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Test Student   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Test Student   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Test Student   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Test Student   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Test Student   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Test Student   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Test Student   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Test Student   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Test Student   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Test Student   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Test Student   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Test Student   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Test Student   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Test Student   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Test Student   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Test Student   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Test Student   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Test Student   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Test Student   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Test Student   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Test Student   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Test Student   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Test Student   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Test Student   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Test Student   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Test Student   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Test Student   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Test Student   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Test Student   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Test Student   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Test Student   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Test Student   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Test Student   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Test Student   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Test Student   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Test Student   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Test Student   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Test Student   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Test Student   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Test Student   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Test Student   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Test Student   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Test Student   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Test Student   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Test Student   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Test Student   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Test Student   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Test Student   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Test Student   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Test Student   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Test Student   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Test Student   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Test Student   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Test Student   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Test Student   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Test Student   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Test Student   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Test Student   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Test Student   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Test Student   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Test Student   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Test Student   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Test Student   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Test Student   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Test Student   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Test Student   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Test Student   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Test Student   Electricity 4.2.1.1 State that there are positive and negative charges : None
Test Student   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Test Student   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Test Student   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Test Student   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Test Student   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Test Student   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Test Student   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Test Student   Electricity 4.2.1.10 Give an account of charging by induction : None
Test Student   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Test Student   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Test Student   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Test Student   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Test Student   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Test Student   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Test Student   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Test Student   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Test Student   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Test Student   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Test Student   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Test Student   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Test Student   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Test Student   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Test Student   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Test Student   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Test Student   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Test Student   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Test Student   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Test Student   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Test Student   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Test Student   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Test Student   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Test Student   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Test Student   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Test Student   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Test Student   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Test Student   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Test Student   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Test Student   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Test Student   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Test Student   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Test Student   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Test Student   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Test Student   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Test Student   Electricity 4.5.2 State that a fuse protects a circuit : None
Test Student   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Test Student   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Maia JAMIESON   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Maia JAMIESON   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Maia JAMIESON   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Maia JAMIESON   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Maia JAMIESON   Motion and Measurement 1.2.1 Define speed : None
Maia JAMIESON   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Maia JAMIESON   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Maia JAMIESON   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Maia JAMIESON   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Maia JAMIESON   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Maia JAMIESON   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Maia JAMIESON   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Maia JAMIESON   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Maia JAMIESON   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Maia JAMIESON   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Maia JAMIESON   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Maia JAMIESON   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Maia JAMIESON   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Maia JAMIESON   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Maia JAMIESON   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Maia JAMIESON   Forces 1.3.3 State that weight is a gravitational force : None
Maia JAMIESON   Forces 1.3.4 Recall and use the equation W = mg : None
Maia JAMIESON   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Maia JAMIESON   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Maia JAMIESON   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Maia JAMIESON   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Maia JAMIESON   Forces 1.4.4 Predict whether an object will float based on density data : None
Maia JAMIESON   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Maia JAMIESON   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Maia JAMIESON   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Maia JAMIESON   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Maia JAMIESON   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Maia JAMIESON   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Maia JAMIESON   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Maia JAMIESON   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Maia JAMIESON   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Maia JAMIESON   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Maia JAMIESON   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Maia JAMIESON   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Maia JAMIESON   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Maia JAMIESON   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Maia JAMIESON   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Maia JAMIESON   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Maia JAMIESON   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Maia JAMIESON   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Maia JAMIESON   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Maia JAMIESON   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Maia JAMIESON   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Maia JAMIESON   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Maia JAMIESON   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Maia JAMIESON   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Maia JAMIESON   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Maia JAMIESON   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Maia JAMIESON   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Maia JAMIESON   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Maia JAMIESON   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Maia JAMIESON   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Maia JAMIESON   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Maia JAMIESON   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Maia JAMIESON   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Maia JAMIESON   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Maia JAMIESON   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Maia JAMIESON   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Maia JAMIESON   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Maia JAMIESON   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Maia JAMIESON   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Maia JAMIESON   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Maia JAMIESON   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Maia JAMIESON   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Maia JAMIESON   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Maia JAMIESON   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Maia JAMIESON   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Maia JAMIESON   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Maia JAMIESON   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Maia JAMIESON   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Maia JAMIESON   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Maia JAMIESON   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Maia JAMIESON   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Maia JAMIESON   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Maia JAMIESON   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Maia JAMIESON   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Maia JAMIESON   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Maia JAMIESON   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Maia JAMIESON   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Maia JAMIESON   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Maia JAMIESON   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Maia JAMIESON   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Maia JAMIESON   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Maia JAMIESON   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Maia JAMIESON   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Maia JAMIESON   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Maia JAMIESON   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Maia JAMIESON   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Maia JAMIESON   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Maia JAMIESON   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Maia JAMIESON   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Maia JAMIESON   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Maia JAMIESON   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Maia JAMIESON   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Maia JAMIESON   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Maia JAMIESON   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Maia JAMIESON   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Maia JAMIESON   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Maia JAMIESON   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Maia JAMIESON   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Maia JAMIESON   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Maia JAMIESON   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Maia JAMIESON   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Maia JAMIESON   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Maia JAMIESON   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Maia JAMIESON   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Maia JAMIESON   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Maia JAMIESON   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Maia JAMIESON   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Maia JAMIESON   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Maia JAMIESON   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Maia JAMIESON   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Maia JAMIESON   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Maia JAMIESON   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Maia JAMIESON   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Maia JAMIESON   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Maia JAMIESON   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Maia JAMIESON   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Maia JAMIESON   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Maia JAMIESON   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Maia JAMIESON   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Maia JAMIESON   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Maia JAMIESON   Electricity 4.2.1.1 State that there are positive and negative charges : None
Maia JAMIESON   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Maia JAMIESON   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Maia JAMIESON   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Maia JAMIESON   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Maia JAMIESON   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Maia JAMIESON   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Maia JAMIESON   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Maia JAMIESON   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Maia JAMIESON   Electricity 4.2.1.10 Give an account of charging by induction : None
Maia JAMIESON   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Maia JAMIESON   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Maia JAMIESON   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Maia JAMIESON   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Maia JAMIESON   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Maia JAMIESON   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Maia JAMIESON   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Maia JAMIESON   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Maia JAMIESON   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Maia JAMIESON   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Maia JAMIESON   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Maia JAMIESON   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Maia JAMIESON   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Maia JAMIESON   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Maia JAMIESON   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Maia JAMIESON   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Maia JAMIESON   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Maia JAMIESON   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Maia JAMIESON   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Maia JAMIESON   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Maia JAMIESON   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Maia JAMIESON   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Maia JAMIESON   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Maia JAMIESON   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Maia JAMIESON   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Maia JAMIESON   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Maia JAMIESON   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Maia JAMIESON   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Maia JAMIESON   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Maia JAMIESON   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Maia JAMIESON   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Maia JAMIESON   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Maia JAMIESON   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Maia JAMIESON   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Maia JAMIESON   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Maia JAMIESON   Electricity 4.5.2 State that a fuse protects a circuit : None
Maia JAMIESON   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Maia JAMIESON   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Natasha POWELL   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Natasha POWELL   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Natasha POWELL   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Natasha POWELL   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Natasha POWELL   Motion and Measurement 1.2.1 Define speed : None
Natasha POWELL   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Natasha POWELL   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Natasha POWELL   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Natasha POWELL   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Natasha POWELL   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Natasha POWELL   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Natasha POWELL   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Natasha POWELL   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Natasha POWELL   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Natasha POWELL   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Natasha POWELL   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Natasha POWELL   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Natasha POWELL   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Natasha POWELL   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Natasha POWELL   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Natasha POWELL   Forces 1.3.3 State that weight is a gravitational force : None
Natasha POWELL   Forces 1.3.4 Recall and use the equation W = mg : None
Natasha POWELL   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Natasha POWELL   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Natasha POWELL   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Natasha POWELL   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Natasha POWELL   Forces 1.4.4 Predict whether an object will float based on density data : None
Natasha POWELL   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Natasha POWELL   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Natasha POWELL   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Natasha POWELL   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Natasha POWELL   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Natasha POWELL   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Natasha POWELL   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Natasha POWELL   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Natasha POWELL   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Natasha POWELL   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Natasha POWELL   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Natasha POWELL   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Natasha POWELL   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Natasha POWELL   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Natasha POWELL   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Natasha POWELL   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Natasha POWELL   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Natasha POWELL   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Natasha POWELL   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Natasha POWELL   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Natasha POWELL   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Natasha POWELL   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Natasha POWELL   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Natasha POWELL   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Natasha POWELL   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Natasha POWELL   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Natasha POWELL   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Natasha POWELL   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Natasha POWELL   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Natasha POWELL   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Natasha POWELL   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Natasha POWELL   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Natasha POWELL   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Natasha POWELL   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Natasha POWELL   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Natasha POWELL   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Natasha POWELL   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Natasha POWELL   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Natasha POWELL   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Natasha POWELL   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Natasha POWELL   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Natasha POWELL   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Natasha POWELL   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Natasha POWELL   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Natasha POWELL   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Natasha POWELL   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Natasha POWELL   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Natasha POWELL   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Natasha POWELL   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Natasha POWELL   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Natasha POWELL   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Natasha POWELL   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Natasha POWELL   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Natasha POWELL   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Natasha POWELL   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Natasha POWELL   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Natasha POWELL   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Natasha POWELL   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Natasha POWELL   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Natasha POWELL   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Natasha POWELL   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Natasha POWELL   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Natasha POWELL   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Natasha POWELL   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Natasha POWELL   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Natasha POWELL   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Natasha POWELL   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Natasha POWELL   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Natasha POWELL   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Natasha POWELL   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Natasha POWELL   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Natasha POWELL   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Natasha POWELL   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Natasha POWELL   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Natasha POWELL   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Natasha POWELL   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Natasha POWELL   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Natasha POWELL   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Natasha POWELL   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Natasha POWELL   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Natasha POWELL   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Natasha POWELL   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Natasha POWELL   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Natasha POWELL   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Natasha POWELL   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Natasha POWELL   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Natasha POWELL   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Natasha POWELL   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Natasha POWELL   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Natasha POWELL   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Natasha POWELL   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Natasha POWELL   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Natasha POWELL   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Natasha POWELL   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Natasha POWELL   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Natasha POWELL   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Natasha POWELL   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Natasha POWELL   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Natasha POWELL   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Natasha POWELL   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Natasha POWELL   Electricity 4.2.1.1 State that there are positive and negative charges : None
Natasha POWELL   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Natasha POWELL   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Natasha POWELL   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Natasha POWELL   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Natasha POWELL   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Natasha POWELL   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Natasha POWELL   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Natasha POWELL   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Natasha POWELL   Electricity 4.2.1.10 Give an account of charging by induction : None
Natasha POWELL   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Natasha POWELL   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Natasha POWELL   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Natasha POWELL   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Natasha POWELL   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Natasha POWELL   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Natasha POWELL   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Natasha POWELL   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Natasha POWELL   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Natasha POWELL   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Natasha POWELL   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Natasha POWELL   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Natasha POWELL   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Natasha POWELL   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Natasha POWELL   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Natasha POWELL   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Natasha POWELL   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Natasha POWELL   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Natasha POWELL   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Natasha POWELL   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Natasha POWELL   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Natasha POWELL   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Natasha POWELL   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Natasha POWELL   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Natasha POWELL   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Natasha POWELL   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Natasha POWELL   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Natasha POWELL   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Natasha POWELL   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Natasha POWELL   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Natasha POWELL   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Natasha POWELL   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Natasha POWELL   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Natasha POWELL   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Natasha POWELL   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Natasha POWELL   Electricity 4.5.2 State that a fuse protects a circuit : None
Natasha POWELL   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Natasha POWELL   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Harris TUNKU HAMMAM   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Harris TUNKU HAMMAM   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Harris TUNKU HAMMAM   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Harris TUNKU HAMMAM   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.1 Define speed : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Harris TUNKU HAMMAM   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Harris TUNKU HAMMAM   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Harris TUNKU HAMMAM   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Harris TUNKU HAMMAM   Forces 1.3.3 State that weight is a gravitational force : None
Harris TUNKU HAMMAM   Forces 1.3.4 Recall and use the equation W = mg : None
Harris TUNKU HAMMAM   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Harris TUNKU HAMMAM   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Harris TUNKU HAMMAM   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Harris TUNKU HAMMAM   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Harris TUNKU HAMMAM   Forces 1.4.4 Predict whether an object will float based on density data : None
Harris TUNKU HAMMAM   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Harris TUNKU HAMMAM   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Harris TUNKU HAMMAM   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Harris TUNKU HAMMAM   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Harris TUNKU HAMMAM   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Harris TUNKU HAMMAM   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Harris TUNKU HAMMAM   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Harris TUNKU HAMMAM   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Harris TUNKU HAMMAM   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Harris TUNKU HAMMAM   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Harris TUNKU HAMMAM   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Harris TUNKU HAMMAM   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Harris TUNKU HAMMAM   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Harris TUNKU HAMMAM   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Harris TUNKU HAMMAM   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Harris TUNKU HAMMAM   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Harris TUNKU HAMMAM   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Harris TUNKU HAMMAM   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Harris TUNKU HAMMAM   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Harris TUNKU HAMMAM   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Harris TUNKU HAMMAM   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Harris TUNKU HAMMAM   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Harris TUNKU HAMMAM   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Harris TUNKU HAMMAM   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Harris TUNKU HAMMAM   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Harris TUNKU HAMMAM   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Harris TUNKU HAMMAM   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Harris TUNKU HAMMAM   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Harris TUNKU HAMMAM   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Harris TUNKU HAMMAM   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Harris TUNKU HAMMAM   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Harris TUNKU HAMMAM   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Harris TUNKU HAMMAM   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Harris TUNKU HAMMAM   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Harris TUNKU HAMMAM   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Harris TUNKU HAMMAM   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Harris TUNKU HAMMAM   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Harris TUNKU HAMMAM   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Harris TUNKU HAMMAM   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Harris TUNKU HAMMAM   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Harris TUNKU HAMMAM   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Harris TUNKU HAMMAM   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Harris TUNKU HAMMAM   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Harris TUNKU HAMMAM   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Harris TUNKU HAMMAM   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Harris TUNKU HAMMAM   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Harris TUNKU HAMMAM   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Harris TUNKU HAMMAM   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Harris TUNKU HAMMAM   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Harris TUNKU HAMMAM   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Harris TUNKU HAMMAM   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Harris TUNKU HAMMAM   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Harris TUNKU HAMMAM   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Harris TUNKU HAMMAM   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Harris TUNKU HAMMAM   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Harris TUNKU HAMMAM   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Harris TUNKU HAMMAM   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Harris TUNKU HAMMAM   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Harris TUNKU HAMMAM   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Harris TUNKU HAMMAM   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Harris TUNKU HAMMAM   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Harris TUNKU HAMMAM   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Harris TUNKU HAMMAM   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Harris TUNKU HAMMAM   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Harris TUNKU HAMMAM   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Harris TUNKU HAMMAM   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Harris TUNKU HAMMAM   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Harris TUNKU HAMMAM   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Harris TUNKU HAMMAM   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Harris TUNKU HAMMAM   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Harris TUNKU HAMMAM   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Harris TUNKU HAMMAM   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Harris TUNKU HAMMAM   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Harris TUNKU HAMMAM   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Harris TUNKU HAMMAM   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Harris TUNKU HAMMAM   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Harris TUNKU HAMMAM   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Harris TUNKU HAMMAM   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Harris TUNKU HAMMAM   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Harris TUNKU HAMMAM   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Harris TUNKU HAMMAM   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Harris TUNKU HAMMAM   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Harris TUNKU HAMMAM   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Harris TUNKU HAMMAM   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Harris TUNKU HAMMAM   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Harris TUNKU HAMMAM   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Harris TUNKU HAMMAM   Electricity 4.2.1.1 State that there are positive and negative charges : None
Harris TUNKU HAMMAM   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Harris TUNKU HAMMAM   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Harris TUNKU HAMMAM   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Harris TUNKU HAMMAM   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Harris TUNKU HAMMAM   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Harris TUNKU HAMMAM   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Harris TUNKU HAMMAM   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Harris TUNKU HAMMAM   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Harris TUNKU HAMMAM   Electricity 4.2.1.10 Give an account of charging by induction : None
Harris TUNKU HAMMAM   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Harris TUNKU HAMMAM   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Harris TUNKU HAMMAM   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Harris TUNKU HAMMAM   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Harris TUNKU HAMMAM   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Harris TUNKU HAMMAM   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Harris TUNKU HAMMAM   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Harris TUNKU HAMMAM   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Harris TUNKU HAMMAM   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Harris TUNKU HAMMAM   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Harris TUNKU HAMMAM   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Harris TUNKU HAMMAM   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Harris TUNKU HAMMAM   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Harris TUNKU HAMMAM   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Harris TUNKU HAMMAM   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Harris TUNKU HAMMAM   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Harris TUNKU HAMMAM   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Harris TUNKU HAMMAM   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Harris TUNKU HAMMAM   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Harris TUNKU HAMMAM   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Harris TUNKU HAMMAM   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Harris TUNKU HAMMAM   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Harris TUNKU HAMMAM   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Harris TUNKU HAMMAM   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Harris TUNKU HAMMAM   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Harris TUNKU HAMMAM   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Harris TUNKU HAMMAM   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Harris TUNKU HAMMAM   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Harris TUNKU HAMMAM   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Harris TUNKU HAMMAM   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Harris TUNKU HAMMAM   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Harris TUNKU HAMMAM   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Harris TUNKU HAMMAM   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Harris TUNKU HAMMAM   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Harris TUNKU HAMMAM   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Harris TUNKU HAMMAM   Electricity 4.5.2 State that a fuse protects a circuit : None
Harris TUNKU HAMMAM   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Harris TUNKU HAMMAM   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Neel TIRATHRAI   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Neel TIRATHRAI   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Neel TIRATHRAI   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Neel TIRATHRAI   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Neel TIRATHRAI   Motion and Measurement 1.2.1 Define speed : None
Neel TIRATHRAI   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Neel TIRATHRAI   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Neel TIRATHRAI   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Neel TIRATHRAI   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Neel TIRATHRAI   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Neel TIRATHRAI   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Neel TIRATHRAI   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Neel TIRATHRAI   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Neel TIRATHRAI   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Neel TIRATHRAI   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Neel TIRATHRAI   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Neel TIRATHRAI   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Neel TIRATHRAI   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Neel TIRATHRAI   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Neel TIRATHRAI   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Neel TIRATHRAI   Forces 1.3.3 State that weight is a gravitational force : None
Neel TIRATHRAI   Forces 1.3.4 Recall and use the equation W = mg : None
Neel TIRATHRAI   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Neel TIRATHRAI   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Neel TIRATHRAI   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Neel TIRATHRAI   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Neel TIRATHRAI   Forces 1.4.4 Predict whether an object will float based on density data : None
Neel TIRATHRAI   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Neel TIRATHRAI   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Neel TIRATHRAI   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Neel TIRATHRAI   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Neel TIRATHRAI   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Neel TIRATHRAI   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Neel TIRATHRAI   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Neel TIRATHRAI   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Neel TIRATHRAI   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Neel TIRATHRAI   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Neel TIRATHRAI   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Neel TIRATHRAI   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Neel TIRATHRAI   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Neel TIRATHRAI   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Neel TIRATHRAI   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Neel TIRATHRAI   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Neel TIRATHRAI   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Neel TIRATHRAI   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Neel TIRATHRAI   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Neel TIRATHRAI   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Neel TIRATHRAI   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Neel TIRATHRAI   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Neel TIRATHRAI   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Neel TIRATHRAI   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Neel TIRATHRAI   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Neel TIRATHRAI   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Neel TIRATHRAI   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Neel TIRATHRAI   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Neel TIRATHRAI   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Neel TIRATHRAI   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Neel TIRATHRAI   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Neel TIRATHRAI   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Neel TIRATHRAI   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Neel TIRATHRAI   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Neel TIRATHRAI   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Neel TIRATHRAI   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Neel TIRATHRAI   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Neel TIRATHRAI   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Neel TIRATHRAI   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Neel TIRATHRAI   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Neel TIRATHRAI   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Neel TIRATHRAI   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Neel TIRATHRAI   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Neel TIRATHRAI   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Neel TIRATHRAI   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Neel TIRATHRAI   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Neel TIRATHRAI   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Neel TIRATHRAI   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Neel TIRATHRAI   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Neel TIRATHRAI   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Neel TIRATHRAI   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Neel TIRATHRAI   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Neel TIRATHRAI   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Neel TIRATHRAI   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Neel TIRATHRAI   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Neel TIRATHRAI   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Neel TIRATHRAI   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Neel TIRATHRAI   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Neel TIRATHRAI   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Neel TIRATHRAI   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Neel TIRATHRAI   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Neel TIRATHRAI   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Neel TIRATHRAI   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Neel TIRATHRAI   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Neel TIRATHRAI   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Neel TIRATHRAI   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Neel TIRATHRAI   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Neel TIRATHRAI   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Neel TIRATHRAI   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Neel TIRATHRAI   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Neel TIRATHRAI   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Neel TIRATHRAI   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Neel TIRATHRAI   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Neel TIRATHRAI   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Neel TIRATHRAI   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Neel TIRATHRAI   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Neel TIRATHRAI   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Neel TIRATHRAI   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Neel TIRATHRAI   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Neel TIRATHRAI   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Neel TIRATHRAI   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Neel TIRATHRAI   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Neel TIRATHRAI   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Neel TIRATHRAI   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Neel TIRATHRAI   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Neel TIRATHRAI   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Neel TIRATHRAI   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Neel TIRATHRAI   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Neel TIRATHRAI   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Neel TIRATHRAI   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Neel TIRATHRAI   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Neel TIRATHRAI   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Neel TIRATHRAI   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Neel TIRATHRAI   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Neel TIRATHRAI   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Neel TIRATHRAI   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Neel TIRATHRAI   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Neel TIRATHRAI   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Neel TIRATHRAI   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Neel TIRATHRAI   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Neel TIRATHRAI   Electricity 4.2.1.1 State that there are positive and negative charges : None
Neel TIRATHRAI   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Neel TIRATHRAI   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Neel TIRATHRAI   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Neel TIRATHRAI   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Neel TIRATHRAI   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Neel TIRATHRAI   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Neel TIRATHRAI   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Neel TIRATHRAI   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Neel TIRATHRAI   Electricity 4.2.1.10 Give an account of charging by induction : None
Neel TIRATHRAI   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Neel TIRATHRAI   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Neel TIRATHRAI   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Neel TIRATHRAI   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Neel TIRATHRAI   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Neel TIRATHRAI   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Neel TIRATHRAI   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Neel TIRATHRAI   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Neel TIRATHRAI   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Neel TIRATHRAI   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Neel TIRATHRAI   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Neel TIRATHRAI   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Neel TIRATHRAI   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Neel TIRATHRAI   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Neel TIRATHRAI   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Neel TIRATHRAI   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Neel TIRATHRAI   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Neel TIRATHRAI   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Neel TIRATHRAI   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Neel TIRATHRAI   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Neel TIRATHRAI   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Neel TIRATHRAI   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Neel TIRATHRAI   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Neel TIRATHRAI   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Neel TIRATHRAI   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Neel TIRATHRAI   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Neel TIRATHRAI   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Neel TIRATHRAI   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Neel TIRATHRAI   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Neel TIRATHRAI   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Neel TIRATHRAI   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Neel TIRATHRAI   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Neel TIRATHRAI   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Neel TIRATHRAI   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Neel TIRATHRAI   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Neel TIRATHRAI   Electricity 4.5.2 State that a fuse protects a circuit : None
Neel TIRATHRAI   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Neel TIRATHRAI   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Jeng Ian ONG   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Jeng Ian ONG   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Jeng Ian ONG   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Jeng Ian ONG   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Jeng Ian ONG   Motion and Measurement 1.2.1 Define speed : None
Jeng Ian ONG   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Jeng Ian ONG   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Jeng Ian ONG   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Jeng Ian ONG   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Jeng Ian ONG   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Jeng Ian ONG   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Jeng Ian ONG   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Jeng Ian ONG   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Jeng Ian ONG   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Jeng Ian ONG   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Jeng Ian ONG   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Jeng Ian ONG   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Jeng Ian ONG   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Jeng Ian ONG   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Jeng Ian ONG   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Jeng Ian ONG   Forces 1.3.3 State that weight is a gravitational force : None
Jeng Ian ONG   Forces 1.3.4 Recall and use the equation W = mg : None
Jeng Ian ONG   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Jeng Ian ONG   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Jeng Ian ONG   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Jeng Ian ONG   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Jeng Ian ONG   Forces 1.4.4 Predict whether an object will float based on density data : None
Jeng Ian ONG   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Jeng Ian ONG   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Jeng Ian ONG   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Jeng Ian ONG   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Jeng Ian ONG   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Jeng Ian ONG   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Jeng Ian ONG   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Jeng Ian ONG   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Jeng Ian ONG   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Jeng Ian ONG   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Jeng Ian ONG   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Jeng Ian ONG   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Jeng Ian ONG   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Jeng Ian ONG   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Jeng Ian ONG   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Jeng Ian ONG   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Jeng Ian ONG   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Jeng Ian ONG   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Jeng Ian ONG   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Jeng Ian ONG   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Jeng Ian ONG   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Jeng Ian ONG   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Jeng Ian ONG   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Jeng Ian ONG   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Jeng Ian ONG   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Jeng Ian ONG   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Jeng Ian ONG   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Jeng Ian ONG   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Jeng Ian ONG   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Jeng Ian ONG   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Jeng Ian ONG   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Jeng Ian ONG   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Jeng Ian ONG   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Jeng Ian ONG   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Jeng Ian ONG   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Jeng Ian ONG   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Jeng Ian ONG   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Jeng Ian ONG   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Jeng Ian ONG   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Jeng Ian ONG   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Jeng Ian ONG   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Jeng Ian ONG   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Jeng Ian ONG   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Jeng Ian ONG   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Jeng Ian ONG   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Jeng Ian ONG   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Jeng Ian ONG   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Jeng Ian ONG   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Jeng Ian ONG   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Jeng Ian ONG   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Jeng Ian ONG   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Jeng Ian ONG   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Jeng Ian ONG   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Jeng Ian ONG   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Jeng Ian ONG   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Jeng Ian ONG   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Jeng Ian ONG   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Jeng Ian ONG   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Jeng Ian ONG   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Jeng Ian ONG   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Jeng Ian ONG   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Jeng Ian ONG   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Jeng Ian ONG   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Jeng Ian ONG   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Jeng Ian ONG   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Jeng Ian ONG   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Jeng Ian ONG   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Jeng Ian ONG   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Jeng Ian ONG   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Jeng Ian ONG   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Jeng Ian ONG   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Jeng Ian ONG   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Jeng Ian ONG   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Jeng Ian ONG   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Jeng Ian ONG   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Jeng Ian ONG   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Jeng Ian ONG   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Jeng Ian ONG   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Jeng Ian ONG   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Jeng Ian ONG   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Jeng Ian ONG   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Jeng Ian ONG   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Jeng Ian ONG   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Jeng Ian ONG   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Jeng Ian ONG   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Jeng Ian ONG   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Jeng Ian ONG   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Jeng Ian ONG   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Jeng Ian ONG   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Jeng Ian ONG   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Jeng Ian ONG   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Jeng Ian ONG   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Jeng Ian ONG   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Jeng Ian ONG   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Jeng Ian ONG   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Jeng Ian ONG   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Jeng Ian ONG   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Jeng Ian ONG   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Jeng Ian ONG   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Jeng Ian ONG   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Jeng Ian ONG   Electricity 4.2.1.1 State that there are positive and negative charges : None
Jeng Ian ONG   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Jeng Ian ONG   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Jeng Ian ONG   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Jeng Ian ONG   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Jeng Ian ONG   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Jeng Ian ONG   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Jeng Ian ONG   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Jeng Ian ONG   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Jeng Ian ONG   Electricity 4.2.1.10 Give an account of charging by induction : None
Jeng Ian ONG   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Jeng Ian ONG   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Jeng Ian ONG   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Jeng Ian ONG   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Jeng Ian ONG   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Jeng Ian ONG   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Jeng Ian ONG   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Jeng Ian ONG   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Jeng Ian ONG   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Jeng Ian ONG   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Jeng Ian ONG   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Jeng Ian ONG   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Jeng Ian ONG   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Jeng Ian ONG   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Jeng Ian ONG   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Jeng Ian ONG   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Jeng Ian ONG   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Jeng Ian ONG   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Jeng Ian ONG   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Jeng Ian ONG   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Jeng Ian ONG   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Jeng Ian ONG   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Jeng Ian ONG   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Jeng Ian ONG   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Jeng Ian ONG   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Jeng Ian ONG   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Jeng Ian ONG   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Jeng Ian ONG   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Jeng Ian ONG   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Jeng Ian ONG   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Jeng Ian ONG   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Jeng Ian ONG   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Jeng Ian ONG   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Jeng Ian ONG   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Jeng Ian ONG   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Jeng Ian ONG   Electricity 4.5.2 State that a fuse protects a circuit : None
Jeng Ian ONG   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Jeng Ian ONG   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Gail CHIN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Gail CHIN   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Gail CHIN   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Gail CHIN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Gail CHIN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Gail CHIN   Forces 1.4.4 Predict whether an object will float based on density data : None
Gail CHIN   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Gail CHIN   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Gail CHIN   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Gail CHIN   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Gail CHIN   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Gail CHIN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Gail CHIN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Gail CHIN   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Gail CHIN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Gail CHIN   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Gail CHIN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Gail CHIN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Gail CHIN   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Gail CHIN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Gail CHIN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Gail CHIN   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Gail CHIN   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Gail CHIN   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Gail CHIN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Gail CHIN   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Rafael ITO   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Rafael ITO   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Rafael ITO   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Rafael ITO   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Rafael ITO   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Rafael ITO   Forces 1.4.4 Predict whether an object will float based on density data : None
Rafael ITO   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Rafael ITO   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Rafael ITO   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Rafael ITO   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Rafael ITO   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Rafael ITO   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Rafael ITO   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Rafael ITO   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Rafael ITO   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Rafael ITO   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Rafael ITO   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Rafael ITO   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Rafael ITO   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Rafael ITO   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Rafael ITO   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Rafael ITO   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Rafael ITO   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Rafael ITO   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Rafael ITO   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Rafael ITO   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Gary BROWN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Gary BROWN   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Gary BROWN   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Gary BROWN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Gary BROWN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Gary BROWN   Forces 1.4.4 Predict whether an object will float based on density data : None
Gary BROWN   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Gary BROWN   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Gary BROWN   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Gary BROWN   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Gary BROWN   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Gary BROWN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Gary BROWN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Gary BROWN   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Gary BROWN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Gary BROWN   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Gary BROWN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Gary BROWN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Gary BROWN   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Gary BROWN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Gary BROWN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Gary BROWN   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Gary BROWN   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Gary BROWN   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Gary BROWN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Gary BROWN   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Ameera BUKHARY   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Ameera BUKHARY   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Ameera BUKHARY   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Ameera BUKHARY   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Ameera BUKHARY   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Ameera BUKHARY   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Ameera BUKHARY   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Ameera BUKHARY   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Ameera BUKHARY   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Ameera BUKHARY   Forces 1.4.4 Predict whether an object will float based on density data : None
Ameera BUKHARY   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Ameera BUKHARY   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Ameera BUKHARY   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Ameera BUKHARY   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Ameera BUKHARY   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Ameera BUKHARY   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Ameera BUKHARY   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Ameera BUKHARY   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Ameera BUKHARY   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Ameera BUKHARY   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Ameera BUKHARY   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Ameera BUKHARY   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Ameera BUKHARY   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Ameera BUKHARY   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Ameera BUKHARY   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Ameera BUKHARY   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Ameera BUKHARY   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Ameera BUKHARY   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Ameera BUKHARY   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Ameera BUKHARY   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Ameera BUKHARY   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Ameera BUKHARY   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Ameera BUKHARY   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Ameera BUKHARY   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Ameera BUKHARY   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Ameera BUKHARY   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Ameera BUKHARY   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Ameera BUKHARY   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Ameera BUKHARY   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Lance SIMANDJOENTAK   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Lance SIMANDJOENTAK   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Lance SIMANDJOENTAK   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Lance SIMANDJOENTAK   Forces 1.4.4 Predict whether an object will float based on density data : None
Lance SIMANDJOENTAK   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Lance SIMANDJOENTAK   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Lance SIMANDJOENTAK   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Lance SIMANDJOENTAK   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Lance SIMANDJOENTAK   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Lance SIMANDJOENTAK   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Lance SIMANDJOENTAK   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Lance SIMANDJOENTAK   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Lance SIMANDJOENTAK   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Lance SIMANDJOENTAK   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Lance SIMANDJOENTAK   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Lance SIMANDJOENTAK   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Lance SIMANDJOENTAK   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Lance SIMANDJOENTAK   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Lance SIMANDJOENTAK   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Lance SIMANDJOENTAK   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Lance SIMANDJOENTAK   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Lance SIMANDJOENTAK   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Lance SIMANDJOENTAK   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Lance SIMANDJOENTAK   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Lance SIMANDJOENTAK   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Lance SIMANDJOENTAK   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Lance SIMANDJOENTAK   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Lance SIMANDJOENTAK   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Lance SIMANDJOENTAK   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Lance SIMANDJOENTAK   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Lance SIMANDJOENTAK   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Lance SIMANDJOENTAK   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Lance SIMANDJOENTAK   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Lance SIMANDJOENTAK   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.1 Define speed : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Lance SIMANDJOENTAK   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Lance SIMANDJOENTAK   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Lance SIMANDJOENTAK   Forces 1.3.3 State that weight is a gravitational force : None
Lance SIMANDJOENTAK   Forces 1.3.4 Recall and use the equation W = mg : None
Lance SIMANDJOENTAK   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Lance SIMANDJOENTAK   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Lance SIMANDJOENTAK   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Lance SIMANDJOENTAK   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Lance SIMANDJOENTAK   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Lance SIMANDJOENTAK   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Lance SIMANDJOENTAK   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Lance SIMANDJOENTAK   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Lance SIMANDJOENTAK   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Lance SIMANDJOENTAK   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Lance SIMANDJOENTAK   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Lance SIMANDJOENTAK   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Lance SIMANDJOENTAK   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Lance SIMANDJOENTAK   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Lance SIMANDJOENTAK   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Lance SIMANDJOENTAK   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Lance SIMANDJOENTAK   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Lance SIMANDJOENTAK   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Lance SIMANDJOENTAK   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Lance SIMANDJOENTAK   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Lance SIMANDJOENTAK   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Lance SIMANDJOENTAK   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Lance SIMANDJOENTAK   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Lance SIMANDJOENTAK   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Lance SIMANDJOENTAK   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Lance SIMANDJOENTAK   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Lance SIMANDJOENTAK   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Lance SIMANDJOENTAK   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Lance SIMANDJOENTAK   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Lance SIMANDJOENTAK   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Lance SIMANDJOENTAK   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Lance SIMANDJOENTAK   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Lance SIMANDJOENTAK   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Lance SIMANDJOENTAK   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Lance SIMANDJOENTAK   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Lance SIMANDJOENTAK   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Lance SIMANDJOENTAK   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Lance SIMANDJOENTAK   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Lance SIMANDJOENTAK   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Lance SIMANDJOENTAK   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Lance SIMANDJOENTAK   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Lance SIMANDJOENTAK   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Lance SIMANDJOENTAK   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Lance SIMANDJOENTAK   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Lance SIMANDJOENTAK   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Lance SIMANDJOENTAK   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Lance SIMANDJOENTAK   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Lance SIMANDJOENTAK   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Lance SIMANDJOENTAK   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Lance SIMANDJOENTAK   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Lance SIMANDJOENTAK   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Lance SIMANDJOENTAK   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Lance SIMANDJOENTAK   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Lance SIMANDJOENTAK   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Lance SIMANDJOENTAK   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Lance SIMANDJOENTAK   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Lance SIMANDJOENTAK   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Lance SIMANDJOENTAK   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Lance SIMANDJOENTAK   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Lance SIMANDJOENTAK   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Lance SIMANDJOENTAK   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Lance SIMANDJOENTAK   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Lance SIMANDJOENTAK   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Lance SIMANDJOENTAK   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Lance SIMANDJOENTAK   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Lance SIMANDJOENTAK   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Lance SIMANDJOENTAK   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Lance SIMANDJOENTAK   Electricity 4.2.1.1 State that there are positive and negative charges : None
Lance SIMANDJOENTAK   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Lance SIMANDJOENTAK   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Lance SIMANDJOENTAK   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Lance SIMANDJOENTAK   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Lance SIMANDJOENTAK   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Lance SIMANDJOENTAK   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Lance SIMANDJOENTAK   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Lance SIMANDJOENTAK   Electricity 4.2.1.10 Give an account of charging by induction : None
Lance SIMANDJOENTAK   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Lance SIMANDJOENTAK   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Lance SIMANDJOENTAK   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Lance SIMANDJOENTAK   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Lance SIMANDJOENTAK   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Lance SIMANDJOENTAK   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Lance SIMANDJOENTAK   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Lance SIMANDJOENTAK   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Lance SIMANDJOENTAK   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Lance SIMANDJOENTAK   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Lance SIMANDJOENTAK   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Lance SIMANDJOENTAK   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Lance SIMANDJOENTAK   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Lance SIMANDJOENTAK   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Lance SIMANDJOENTAK   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Lance SIMANDJOENTAK   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Lance SIMANDJOENTAK   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Lance SIMANDJOENTAK   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Lance SIMANDJOENTAK   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Lance SIMANDJOENTAK   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Lance SIMANDJOENTAK   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Lance SIMANDJOENTAK   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Lance SIMANDJOENTAK   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Lance SIMANDJOENTAK   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Lance SIMANDJOENTAK   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Lance SIMANDJOENTAK   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Lance SIMANDJOENTAK   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Lance SIMANDJOENTAK   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Lance SIMANDJOENTAK   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Lance SIMANDJOENTAK   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Lance SIMANDJOENTAK   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Lance SIMANDJOENTAK   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Lance SIMANDJOENTAK   Electricity 4.5.2 State that a fuse protects a circuit : None
Lance SIMANDJOENTAK   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Lance SIMANDJOENTAK   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Arshi JAIN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Arshi JAIN   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Arshi JAIN   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Arshi JAIN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Arshi JAIN   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Arshi JAIN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Arshi JAIN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Arshi JAIN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Arshi JAIN   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Arshi JAIN   Forces 1.4.4 Predict whether an object will float based on density data : None
Arshi JAIN   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Arshi JAIN   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Arshi JAIN   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Arshi JAIN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Arshi JAIN   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Arshi JAIN   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Arshi JAIN   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Arshi JAIN   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Arshi JAIN   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Arshi JAIN   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Arshi JAIN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Arshi JAIN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Arshi JAIN   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Arshi JAIN   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Arshi JAIN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Arshi JAIN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Arshi JAIN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Arshi JAIN   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Arshi JAIN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Arshi JAIN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Arshi JAIN   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Arshi JAIN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Arshi JAIN   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Arshi JAIN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Arshi JAIN   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Arshi JAIN   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Arshi JAIN   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Arshi JAIN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Arshi JAIN   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Vira VERKHEDKAR   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Vira VERKHEDKAR   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Vira VERKHEDKAR   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Vira VERKHEDKAR   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Vira VERKHEDKAR   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Vira VERKHEDKAR   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Vira VERKHEDKAR   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Vira VERKHEDKAR   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Vira VERKHEDKAR   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Vira VERKHEDKAR   Forces 1.4.4 Predict whether an object will float based on density data : None
Vira VERKHEDKAR   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Vira VERKHEDKAR   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Vira VERKHEDKAR   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Vira VERKHEDKAR   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Vira VERKHEDKAR   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Vira VERKHEDKAR   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Vira VERKHEDKAR   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Vira VERKHEDKAR   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Vira VERKHEDKAR   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Vira VERKHEDKAR   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Vira VERKHEDKAR   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Vira VERKHEDKAR   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Vira VERKHEDKAR   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Vira VERKHEDKAR   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Vira VERKHEDKAR   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Vira VERKHEDKAR   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Vira VERKHEDKAR   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Vira VERKHEDKAR   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Vira VERKHEDKAR   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Vira VERKHEDKAR   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Vira VERKHEDKAR   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Vira VERKHEDKAR   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Vira VERKHEDKAR   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Vira VERKHEDKAR   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Vira VERKHEDKAR   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Vira VERKHEDKAR   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Vira VERKHEDKAR   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Vira VERKHEDKAR   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Vira VERKHEDKAR   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Ameera BUKHARY   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Ameera BUKHARY   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Ameera BUKHARY   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Ameera BUKHARY   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Ameera BUKHARY   Motion and Measurement 1.2.1 Define speed : None
Ameera BUKHARY   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Ameera BUKHARY   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Ameera BUKHARY   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Ameera BUKHARY   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Ameera BUKHARY   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Ameera BUKHARY   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Ameera BUKHARY   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Ameera BUKHARY   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Ameera BUKHARY   Forces 1.3.3 State that weight is a gravitational force : None
Ameera BUKHARY   Forces 1.3.4 Recall and use the equation W = mg : None
Ameera BUKHARY   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Ameera BUKHARY   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Ameera BUKHARY   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Ameera BUKHARY   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Ameera BUKHARY   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Ameera BUKHARY   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Ameera BUKHARY   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Ameera BUKHARY   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Ameera BUKHARY   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Ameera BUKHARY   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Ameera BUKHARY   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Ameera BUKHARY   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Ameera BUKHARY   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Ameera BUKHARY   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Ameera BUKHARY   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Ameera BUKHARY   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Ameera BUKHARY   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Ameera BUKHARY   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Ameera BUKHARY   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Ameera BUKHARY   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Ameera BUKHARY   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Ameera BUKHARY   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Ameera BUKHARY   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Ameera BUKHARY   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Ameera BUKHARY   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Ameera BUKHARY   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Ameera BUKHARY   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Ameera BUKHARY   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Ameera BUKHARY   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Ameera BUKHARY   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Ameera BUKHARY   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Ameera BUKHARY   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Ameera BUKHARY   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Ameera BUKHARY   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Ameera BUKHARY   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Ameera BUKHARY   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Ameera BUKHARY   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Ameera BUKHARY   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Ameera BUKHARY   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Ameera BUKHARY   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Ameera BUKHARY   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Ameera BUKHARY   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Ameera BUKHARY   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Ameera BUKHARY   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Ameera BUKHARY   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Ameera BUKHARY   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Ameera BUKHARY   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Ameera BUKHARY   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Ameera BUKHARY   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Ameera BUKHARY   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Ameera BUKHARY   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Ameera BUKHARY   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Ameera BUKHARY   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Ameera BUKHARY   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Ameera BUKHARY   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Ameera BUKHARY   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Ameera BUKHARY   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Ameera BUKHARY   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Ameera BUKHARY   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Ameera BUKHARY   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Ameera BUKHARY   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Ameera BUKHARY   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Ameera BUKHARY   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Ameera BUKHARY   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Ameera BUKHARY   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Ameera BUKHARY   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Ameera BUKHARY   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Ameera BUKHARY   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Ameera BUKHARY   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Ameera BUKHARY   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Ameera BUKHARY   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Ameera BUKHARY   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Ameera BUKHARY   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Ameera BUKHARY   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Ameera BUKHARY   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Ameera BUKHARY   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Ameera BUKHARY   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Ameera BUKHARY   Electricity 4.2.1.1 State that there are positive and negative charges : None
Ameera BUKHARY   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Ameera BUKHARY   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Ameera BUKHARY   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Ameera BUKHARY   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Ameera BUKHARY   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Ameera BUKHARY   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Ameera BUKHARY   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Ameera BUKHARY   Electricity 4.2.1.10 Give an account of charging by induction : None
Ameera BUKHARY   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Ameera BUKHARY   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Ameera BUKHARY   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Ameera BUKHARY   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Ameera BUKHARY   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Ameera BUKHARY   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Ameera BUKHARY   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Ameera BUKHARY   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Ameera BUKHARY   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Ameera BUKHARY   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Ameera BUKHARY   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Ameera BUKHARY   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Ameera BUKHARY   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Ameera BUKHARY   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Ameera BUKHARY   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Ameera BUKHARY   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Ameera BUKHARY   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Ameera BUKHARY   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Ameera BUKHARY   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Ameera BUKHARY   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Ameera BUKHARY   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Ameera BUKHARY   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Ameera BUKHARY   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Ameera BUKHARY   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Ameera BUKHARY   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Ameera BUKHARY   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Ameera BUKHARY   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Ameera BUKHARY   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Ameera BUKHARY   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Ameera BUKHARY   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Ameera BUKHARY   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Ameera BUKHARY   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Ameera BUKHARY   Electricity 4.5.2 State that a fuse protects a circuit : None
Ameera BUKHARY   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Ameera BUKHARY   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Nixon CHUNG   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Nixon CHUNG   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Nixon CHUNG   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Nixon CHUNG   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Nixon CHUNG   Motion and Measurement 1.2.1 Define speed : None
Nixon CHUNG   Motion and Measurement 1.2.2 Calculate Average speed from total distance / total time : None
Nixon CHUNG   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Nixon CHUNG   Motion and Measurement 1.2.4 Plot and interpret a speed / time graph. : None
Nixon CHUNG   Motion and Measurement 1.2.5 Be able to label points on a speed / time graph, from the shape graph, when a body is (a) at rest, (b) moving with constant speed, (c) moving with changing speed : None
Nixon CHUNG   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Nixon CHUNG   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Nixon CHUNG   Motion and Measurement 1.2.8 Define and Calculate acceleration.
State that deceleration is a negative acceleration : None
Nixon CHUNG   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Nixon CHUNG   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Nixon CHUNG   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Nixon CHUNG   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Nixon CHUNG   Motion and Measurement 1.2.13 Describe qualitatively the motion of bodies falling in a uniform gravitational field without air resistance. : None
Nixon CHUNG   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Nixon CHUNG   Forces 1.3.1 Explain that In the absence of an unbalanced force, an object will either remain at rest or travel with a constant speed in a straight line. Unbalanced forces change motion. : None
Nixon CHUNG   Forces 1.3.2 Demonstrate an understanding that mass is a property that ‘resists’ change in motion
Distinguish between mass and weight
Describe in detail how weights (and hence masses) may be compared using a balance : None
Nixon CHUNG   Forces 1.3.3 State that weight is a gravitational force : None
Nixon CHUNG   Forces 1.3.4 Recall and use the equation W = mg : None
Nixon CHUNG   Forces 1.3.5 Describe, and use the concept of, weight as the effect of a gravitational field on a mass : None
Nixon CHUNG   Forces 1.4.1 Recall and use the equation ρ = m/V : None
Nixon CHUNG   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Nixon CHUNG   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Nixon CHUNG   Forces 1.4.4 Predict whether an object will float based on density data : None
Nixon CHUNG   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Nixon CHUNG   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Nixon CHUNG   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Nixon CHUNG   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Nixon CHUNG   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Nixon CHUNG   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Nixon CHUNG   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Nixon CHUNG   Forces 1.5.8 Add vectors by graphical representation to determine a resultant– the parallelogram of forces : None
Nixon CHUNG   Forces 1.5.9 Determine graphically the resultant of two vectors– draw scale vector diagrams for two forces at an angle to each other, measure then calculate the resultant. : None
Nixon CHUNG   Forces 1.5.10 Describe qualitatively(without the need to do calculations) motion in a curved path due to a perpendicular force. (Acceleration with no change in speed) Centripetal force(not the equation but state the effect of changing mass, speed and radius) and what causes the centripetal force in different situations. : None
Nixon CHUNG   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Nixon CHUNG   Forces 1.5.12 Be able to describe and to do calculations to show that increasing the force or the distance from a pivot increases the moment of a force
 Calculate moment using the equation:
 Moment = force × perpendicular distance from the pivot
 Apply the principle of moments to the balancing of a beam about a pivot : None
Nixon CHUNG   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Nixon CHUNG   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Nixon CHUNG   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Nixon CHUNG   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Nixon CHUNG   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Nixon CHUNG   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Nixon CHUNG   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Nixon CHUNG   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Nixon CHUNG   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Nixon CHUNG   Light and waves 3.2.5 Describe an experimental demonstration of the refraction of light
 (draw a diagram and label apparatus) : None
Nixon CHUNG   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Nixon CHUNG   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Nixon CHUNG   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Nixon CHUNG   Light and waves 3.2.9 Give the meaning of critical angle (Link this to the equation n = sin i / sin r)
 Recall and use n = 1 / sin c : None
Nixon CHUNG   Light and waves 3.2.10 Describe internal and total internal reflection
 (Draw a diagram and state the reason it happens) : None
Nixon CHUNG   Light and waves 3.2.11 Describe the action of optical fibres particularly in:
 Medicine and Communications technology : None
Nixon CHUNG   Light and waves 3.2.12 Describe the action of a thin converging lens on a beam of light.
 (Draw a diagram and describe)
 Use the term principal focus and focal length. (Label these points on the diagram) : None
Nixon CHUNG   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Nixon CHUNG   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Nixon CHUNG   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Nixon CHUNG   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Nixon CHUNG   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Nixon CHUNG   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Nixon CHUNG   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Nixon CHUNG   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Nixon CHUNG   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Nixon CHUNG   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Nixon CHUNG   Light and waves 3.2.5 Describe the use of water waves to show: (Labelled diagram of the apparatus)
 – reflection at a plane surface
 – refraction due to a change of speed
 – diffraction produced by wide and narrow gaps : None
Nixon CHUNG   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Nixon CHUNG   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Nixon CHUNG   Light and waves 3.2.8 Describe the main features of the electromagnetic spectrum (There are 3 statements to learn) and state that all e.m. waves travel with the same high speed in a vacuum : None
Nixon CHUNG   Light and waves 3.2.9 Describe typical properties and uses of radiations in all the different regions of the electromagnetic spectrum including:
 – radio and television communications (radio waves)
 – satellite television and telephones (microwaves)
 – electrical appliances, remote controllers for televisions and intruder alarms (infrared)
 – medicine and security (X-rays) : None
Nixon CHUNG   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Nixon CHUNG   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Nixon CHUNG   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Nixon CHUNG   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Nixon CHUNG   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Nixon CHUNG   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Nixon CHUNG   Light and waves 3.2.16 Relate (Draw labelled diagrams)
 · loudness to amplitude
 · and pitch to frequency of sound waves : None
Nixon CHUNG   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Nixon CHUNG   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Nixon CHUNG   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Nixon CHUNG   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Nixon CHUNG   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Nixon CHUNG   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Nixon CHUNG   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Nixon CHUNG   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Nixon CHUNG   Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
 : None
Nixon CHUNG   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Nixon CHUNG   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Nixon CHUNG   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Nixon CHUNG   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Nixon CHUNG   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Nixon CHUNG   Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
 : None
Nixon CHUNG   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Nixon CHUNG   Work energy and power 1.7.11 Show a qualitative understanding of efficiency
 : None
Nixon CHUNG   Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
 : None
Nixon CHUNG   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Nixon CHUNG   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Nixon CHUNG   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Nixon CHUNG   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Nixon CHUNG   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Nixon CHUNG   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Nixon CHUNG   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Nixon CHUNG   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Nixon CHUNG   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Nixon CHUNG   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Nixon CHUNG   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Nixon CHUNG   Thermal processes 2.3.2 b) Give a simple molecular account of conduction in solids including lattice vibration and transfer by electrons : None
Nixon CHUNG   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Nixon CHUNG   Thermal processes 2.3.4 d) Relate convection in fluids to density changes and describe experiments to illustrate convection : None
Nixon CHUNG   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Nixon CHUNG   Thermal processes 2.3.6 f) Recognise that thermal energy transfer by radiation does not require a medium : None
Nixon CHUNG   Thermal processes 2.3.7 g) Describe the effect of surface colour (black or white) and texture (dull or shiny) on the emission, absorption and reflection of radiation : None
Nixon CHUNG   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Nixon CHUNG   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Nixon CHUNG   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Nixon CHUNG   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Nixon CHUNG   Forces 1.6.2 b) Recall and use the equation momentum = mass × velocity, p=mv : None
Nixon CHUNG   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Nixon CHUNG   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Nixon CHUNG   Electricity 4.2.5.1 State that resistance = p.d./current and understand qualitatively how changes in p.d. or resistance affect current : None
Nixon CHUNG   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Nixon CHUNG   Electricity 4.2.5.3 Describe an experiment to determine resistance : None
Nixon CHUNG   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Nixon CHUNG   Electricity 4.2.5.5 Relate (without calculation) the resistance of a wire to its length and to its diameter : None
Nixon CHUNG   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Nixon CHUNG   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Nixon CHUNG   Electricity 4.2.1.1 State that there are positive and negative charges : None
Nixon CHUNG   Electricity 4.2.1.2 State that unlike charges attract and that like charges repel : None
Nixon CHUNG   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Nixon CHUNG   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Nixon CHUNG   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Nixon CHUNG   Electricity 4.2.1.6 State that charge is measured in coulombs : None
Nixon CHUNG   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Nixon CHUNG   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Nixon CHUNG   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Nixon CHUNG   Electricity 4.2.1.10 Give an account of charging by induction : None
Nixon CHUNG   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Nixon CHUNG   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Nixon CHUNG   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Nixon CHUNG   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Nixon CHUNG   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Nixon CHUNG   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Nixon CHUNG   Electricity 4.2.3.1 State that the e.m.f. of an electrical source of energy is measured in volts : None
Nixon CHUNG   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Nixon CHUNG   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Nixon CHUNG   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Nixon CHUNG   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Nixon CHUNG   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Nixon CHUNG   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Nixon CHUNG   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Nixon CHUNG   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Nixon CHUNG   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Nixon CHUNG   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Nixon CHUNG   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Nixon CHUNG   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Nixon CHUNG   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Nixon CHUNG   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Nixon CHUNG   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Nixon CHUNG   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Nixon CHUNG   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Nixon CHUNG   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Nixon CHUNG   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Nixon CHUNG   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Nixon CHUNG   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Nixon CHUNG   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Nixon CHUNG   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Nixon CHUNG   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Nixon CHUNG   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Nixon CHUNG   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Nixon CHUNG   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Nixon CHUNG   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Nixon CHUNG   Electricity 4.5.2 State that a fuse protects a circuit : None
Nixon CHUNG   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Nixon CHUNG   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Gary BROWN   Motion and Measurement 1.1.2 Use and describe the use of clocks and devices, both analogue and digital, for measuring an interval of time : None
Gary BROWN   Motion and Measurement 1.1.3 Obtain an average value for a small distance and for a short interval of time by measuring multiples (including the period of a pendulum) : None
Gary BROWN   Motion and Measurement 1.1.3 Understand that a micrometer screw gauge is used to measure very small distances : None
Gary BROWN   Motion and Measurement 1.2.1 Define speed : None
Gary BROWN   Motion and Measurement 1.2.7 Distinguish between speed and velocity. : None
Gary BROWN   Motion and Measurement 1.2.10 State that the acceleration of free fall for a body near to the Earth is constant. (10m/s2) : None
Gary BROWN   Motion and Measurement 1.2.11 Recognise linear motion for which the acceleration is constant. : None
Gary BROWN   Motion and Measurement 1.2.12 Recognise motion for which the acceleration is not constant. : None
Gary BROWN   Forces 1.3.3 State that weight is a gravitational force : None
Gary BROWN   Forces 1.3.4 Recall and use the equation W = mg : None
Gary BROWN   Forces 1.4.2 Describe an experiment to determine the density of a liquid and of a regularly shaped solid and make the necessary calculation : None
Gary BROWN   Forces 1.4.3 Describe the determination of the density of an irregularly shaped solid by the method of displacement : None
Gary BROWN   Forces 1.5.1 Describe the ways in which a force may change the motion of a body : None
Gary BROWN   Forces 1.5.3 State that a force may produce a change in size and shape of a body : None
Gary BROWN   Forces 1.5.4 Plot extension/load graphs and describe the associated experimental procedure
 Interpret extension/load graphs : None
Gary BROWN   Forces 1.5.5 State Hooke’s Law, Recall the expression F = k x, Use the equation : None
Gary BROWN   Forces 1.5.6 Explain what is meant by the term ‘limit of proportionality’ for an extension/load graph : None
Gary BROWN   Forces 1.5.11 Describe the moment of a force as a measure of its turning effect and give everyday examples : None
Gary BROWN   Forces 1.5.13 Conditions for equilibrium: State that for a system is in equilibrium there is no resultant turning effect and there is no resultant force. : None
Gary BROWN   Forces 1.5.14 Perform and describe an experiment (involving vertical forces) to show that there is no net moment on a body in equilibrium : None
Gary BROWN   Forces 1.5.15 Apply the idea of opposing moments to simple systems in equilibrium : None
Gary BROWN   Forces 1.5.16 Centre of mass - Perform and describe an experiment to determine the position of the centre of mass of a plane lamina(any shape flat piece of material). : None
Gary BROWN   Forces 1.5.17 Describe qualitatively the effect of the position of the centre of mass on the stability of simple objects. : None
Gary BROWN   Light and waves 3.2.1 Describe the formation of an optical image by a plane mirror, and give its characteristics. (Draw a ray diagram and describe the image) : None
Gary BROWN   Light and waves 3.2.2 Recall and use the law angle of incidence = angle of reflection : None
Gary BROWN   Light and waves 3.2.3 Recall that the image in a plane mirror is virtual : None
Gary BROWN   Light and waves 3.2.4 Perform simple constructions, measurements and calculations : None
Gary BROWN   Light and waves 3.2.6 Use the terminology for the angle of incidence, I, and angle of refraction, r, and describe the passage of light through parallel-sided transparent material.
 (Draw a diagram and label) : None
Gary BROWN   Light and waves 3.2.8 Recall and use the equation:
 sin i /sin r = n : None
Gary BROWN   Light and waves 3.2.13 State what the terms real image and virtual image mean : None
Gary BROWN   Light and waves 3.2.14 Draw ray diagrams to illustrate the formation of a real image by a single lens : None
Gary BROWN   Light and waves 3.2.15 Draw ray diagrams to illustrate the formation of a virtual image by a single lens
Describe the nature of an image using the terms enlarged/same size/diminished and upright/inverted : None
Gary BROWN   Light and waves 3.2.16 Use and describe the use of a single lens as a magnifying glass : None
Gary BROWN   Light and waves 3.2.17 Give a qualitative account of the dispersion of light as shown by the action on light of a glass prism. (Draw a diagram, label the colours, state why dispersion occurs) : None
Gary BROWN   Light and waves 3.2.18 Recall that light of a single frequency is described as monochromatic : None
Gary BROWN   Light and waves 3.2.1 State how you know that wave motion transfers energy without transferring matter in the direction of wave travel. : None
Gary BROWN   Light and waves 3.2.2 Describe what is meant by wave motion as illustrated by vibration in ropes and springs and by experiments using water waves : None
Gary BROWN   Light and waves 3.2.3 Use the term wavefront (Draw a diagram and state what the word means) : None
Gary BROWN   Light and waves 3.2.6 Interpret reflection, refraction and diffraction using wave theory
 (Explain what happens to the waves in each case) : None
Gary BROWN   Light and waves 3.2.10 State the safety issues regarding the use of:
 · microwaves
 · and X rays : None
Gary BROWN   Light and waves 3.2.12 Use the term monochromatic(also part of the light section)
 (Learn and state what it means) : None
Gary BROWN   Light and waves 3.2.13 Describe the production of sound by vibrating sources
 (Give examples of how sounds are made and state what is vibrating) : None
Gary BROWN   Light and waves 3.2.15 Describe compression and rarefaction(Draw a labelled diagram) : None
Gary BROWN   Light and waves 3.2.17 State the approximate range of audible frequencies for a healthy human is 20Hz to 20000Hz
 (You need to learn these numbers) : None
Gary BROWN   Light and waves 3.2.18 Show an understanding that a medium is needed to transmit sound waves
 (Describe the experiment which proves this) : None
Gary BROWN   Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
 : None
Gary BROWN   Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
 : None
Gary BROWN   Work energy and power 1.7.5 Describe energy changes in terms of work done
 : None
Gary BROWN   Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
 : None
Gary BROWN   Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
 : None
Gary BROWN   Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
 : None
Gary BROWN   Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
 : None
Gary BROWN   Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
 : None
Gary BROWN   Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
 : None
Gary BROWN   Pressure and density 1.8.2 b) Relate pressure to force and area, using appropriate examples : None
Gary BROWN   Pressure and density 1.8.3 c) Describe the simple mercury barometer and its uses in measuring atmospheric pressure : None
Gary BROWN   Pressure and density 1.8.4 d) Relate (without calculation) the pressure beneath a liquid surface to depth and to density, using appropriate examples : None
Gary BROWN   Pressure and density 1.8.5 e) Use and describe the use of a manometer : None
Gary BROWN   Thermal processes 2.3.1 a) Describe experiments to demonstrate the properties of good and bad thermal conductors : None
Gary BROWN   Thermal processes 2.3.3 c) Recognise convection as an important method of thermal transfer in fluids : None
Gary BROWN   Thermal processes 2.3.5 e) Identify infra-red radiation as part of the electromagnetic spectrum : None
Gary BROWN   Thermal processes 2.3.8 h) Describe experiments to show the properties of good and bad emitters and good and bad absorbers of infra-red radiation : None
Gary BROWN   Thermal processes 2.3.9 I) Show understanding that the amount of radiation emitted also depends on the surface temperature and surface area of a body : None
Gary BROWN   Thermal processes 2.3.10 j) Identify and explain some of the everyday applications and consequences of conduction, convection and radiation : None
Gary BROWN   Forces 1.6.4 d) Apply the principle of the conservation of momentum to solve simple problems in one dimension : None
Gary BROWN   Electricity 4.2.5.2 Recall and use the equation R = V/I : None
Gary BROWN   Electricity 4.2.5.4 using a voltmeter and an ammeter : None
Gary BROWN   Electricity 4.2.5.6 Sketch and explain the current-voltage characteristic of an ohmic resistor and a filament lamp : None
Gary BROWN   Electricity 4.2.5.7 Recall and use quantitatively the proportionality between resistance and length, and the inverse proportionality between resistance and cross-sectional area of a wire : None
Gary BROWN   Electricity 4.2.1.1 State that there are positive and negative charges : None
Gary BROWN   Electricity 4.2.1.3 Describe simple experiments to show the production and detection of electrostatic charges : None
Gary BROWN   Electricity 4.2.1.4 State that charging a body involves the addition or removal of electrons : None
Gary BROWN   Electricity 4.2.1.5 Distinguish between electrical conductors and insulators and give typical examples : None
Gary BROWN   Electricity 4.2.1.7 State that the direction of an electric field at a point is the direction of the force on a positive charge at that point : None
Gary BROWN   Electricity 4.2.1.8 Describe an electric field as a region in which an electric charge experiences a force : None
Gary BROWN   Electricity 4.2.1.9 Describe simple field patterns, including the field around a point charge, the field around a charged conducting sphere and the field between two parallel plates (not including end effects) : None
Gary BROWN   Electricity 4.2.1.10 Give an account of charging by induction : None
Gary BROWN   Electricity 4.2.1.11 Recall and use a simple electron model to distinguish between conductors and insulators : None
Gary BROWN   Electricity 4.2.1.2 Use and describe the use of an ammeter, both analogue and digital : None
Gary BROWN   Electricity 4.2.1.3 State that current in metals is due to a flow of electrons : None
Gary BROWN   Electricity 4.2.1.5 Distinguish between the direction of flow of electrons and conventional current : None
Gary BROWN   Electricity 4.2.3.2 Show understanding that e.m.f. is defined in terms of energy supplied by a source in driving charge round a complete circuit : None
Gary BROWN   Electricity 4.2.4.1 State that the potential difference (p.d.) across a circuit component is measured in volts : None
Gary BROWN   Electricity 4.2.4.2 Use and describe the use of a voltmeter, both analogue and digital : None
Gary BROWN   Electricity 4.2.4.3 Recall that 1V is equivalent to 1 J/C : None
Gary BROWN   Electricity 4.2.6.1 Understand that electric circuits transfer energy from the battery or power source to the circuit components then into the surroundings : None
Gary BROWN   Electricity 4.2.6.2 Recall and use the equations P = IV and E = IVt : None
Gary BROWN   Electricity 4.3.1.1 Draw and interpret circuit diagrams containing sources, switches, resistors (fixed and variable), heaters, thermistors, light-dependent resistors, lamps, ammeters, voltmeters, galvanometers, magnetising coils, transformers, bells, fuses and relays : None
Gary BROWN   Electricity 4.3.1.2 Draw and interpret circuit diagrams containing diodes : None
Gary BROWN   Electricity 4.3.3.1 Understand that the current at every point in a series circuit is the same : None
Gary BROWN   Electricity 4.3.3.2 Give the combined resistance of two or more resistors in series : None
Gary BROWN   Electricity 4.3.3.3 State that, for a parallel circuit, the current from the source is larger than the current in each branch : None
Gary BROWN   Electricity 4.3.3.4 State that the combined resistance of two resistors in parallel is less than that of either resistor by itself : None
Gary BROWN   Electricity 4.3.3.5 State the advantages of connecting lamps in parallel in a lighting circuit : None
Gary BROWN   Electricity 4.3.3.6 Calculate the combined e.m.f. of several sources in series : None
Gary BROWN   Electricity 4.3.3.7 Recall and use the fact that the sum of the p.d.s across the components in a series circuit is equal to the total p.d. across the supply : None
Gary BROWN   Electricity 4.3.3.8 Recall and use the fact that the current from the source is the sum of the currents in the separate branches of a parallel circuit : None
Gary BROWN   Electricity 4.3.3.9 Calculate the effective resistance of two resistors in parallel : None
Gary BROWN   Electricity 4.3.3.1 Describe the action of a variable potential divider (potentiometer) : None
Gary BROWN   Electricity 4.3.3.2 Describe the action of thermistors and light- dependent resistors and show understanding of their use as input transducers : None
Gary BROWN   Electricity 4.3.3.3 Describe the action of a relay and show understanding of its use in switching circuits : None
Gary BROWN   Electricity 4.3.3.4 Describe the action of a diode and show understanding of its use as a rectifier : None
Gary BROWN   Electricity 4.3.3.5 Recognise and show understanding of circuits operating as light-sensitive switches and temperature-operated alarms (to include the use of a relay) : None
Gary BROWN   Electricity 4.4.1 Explain and use the terms analogue and digital in terms of continuous variation and high/low states : None
Gary BROWN   Electricity 4.4.2 Describe the action of NOT, AND, OR, NAND and NOR gates : None
Gary BROWN   Electricity 4.4.3 Recall and use the symbols for logic gates : None
Gary BROWN   Electricity 4.4.4 Design and understand simple digital circuits combining several logic gates : None
Gary BROWN   Electricity 4.4.5 Use truth tables to describe the action of individual gates and simple combinations of gates : None
Gary BROWN   Electricity 4.5.1 State the hazards of: damaged insulation, overheating of cables, damp conditions : None
Gary BROWN   Electricity 4.5.2 State that a fuse protects a circuit : None
Gary BROWN   Electricity 4.5.3 Explain the use of fuses and circuit breakers and choose appropriate fuse ratings and circuit-breaker settings : None
Gary BROWN   Electricity 4.5.4 Explain the benefits of earthing metal cases : None
Test Student   None : Motion and Measurement: Measurement Techniques
Test Student   None : Motion and Measurement: Motion calculations
Test Student   None : Motion and Measurement: Motion graphs
Test Student   None : Motion and Measurement: Falling bodies
Test Student   None : Light and waves: Refraction
Test Student   None : Light and waves: Lenses
Test Student   None : Light and waves: Sound
Test Student   None : Light and waves: Reflection
Test Student   None : Forces: Newton's Laws
Test Student   Test: First topic 1 First topic, first sub topic, first point : None
Test Student   Test: First topic 2 First topic, first sub topic, second point : None
Marie AAMANN   None : Motion and Measurement: Motion calculations
entries = StudentJournalEntry.objects.filter(entry is not Null)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'Null' is not defined
entries = StudentJournalEntry.objects.filter(entry is not Blank)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'Blank' is not defined
entries = StudentJournalEntry.objects.filter(entry is not blank)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'blank' is not defined
entries = StudentJournalEntry.objects.filter(entry is not null)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'null' is not defined
entries = StudentJournalEntry.objects.filter(entry__isnull=False)
for entry in entries:
    print(entry.student, " ", entry.syllabus_point, ":", entry.syllabus_sub_topic)
Gail CHIN   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Marie AAMANN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Marie AAMANN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Marie AAMANN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Marie AAMANN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Marie AAMANN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Marie AAMANN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Marie AAMANN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Marie AAMANN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Marie AAMANN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Marie AAMANN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Marie AAMANN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Marie AAMANN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Marie AAMANN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Marie AAMANN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Marie AAMANN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Marie AAMANN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Nixon CHUNG   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Nixon CHUNG   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Nixon CHUNG   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Nixon CHUNG   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Nixon CHUNG   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Nixon CHUNG   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Nixon CHUNG   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Nixon CHUNG   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Nixon CHUNG   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Nixon CHUNG   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Nixon CHUNG   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Nixon CHUNG   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Nixon CHUNG   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Nixon CHUNG   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Nixon CHUNG   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
Test Student   None : Motion and Measurement: Motion calculations
Test Student   None : Motion and Measurement: Falling bodies
entries = StudentJournalEntry.objects.filter(entry__isnull=False, syllabus_sub_topic__isnull=False)
entries
<QuerySet [<StudentJournalEntry: StudentJournalEntry object (2481)>, <StudentJournalEntry: StudentJournalEntry object (2483)>]>
for entry in entries:
    print(entry.student, " ", entry.syllabus_point, ":", entry.syllabus_sub_topic)
Test Student   None : Motion and Measurement: Motion calculations
Test Student   None : Motion and Measurement: Falling bodies
entries = StudentJournalEntry.objects.filter(entry__isnull=False, syllabus_sub_topic__isnull=True)
for entry in entries:
    print(entry.student, " ", entry.syllabus_point, ":", entry.syllabus_sub_topic)
Gail CHIN   Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume : None
Marie AAMANN   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Marie AAMANN   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Marie AAMANN   Light and waves 3.2.21 Describe an experiment to determine the speed of sound in air
 (Draw a labelled diagram. State the measurements and calculations you need.) : None
Marie AAMANN   Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
 : None
Marie AAMANN   Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
 : None
Marie AAMANN   Motion and Measurement 1.2.3 Plot and interpret a distance / time graph. : None
Marie AAMANN   Motion and Measurement 1.2.6 Calculate the area under a speed / time graph to determine the distance travelled for motion with constant acceleration : None
Marie AAMANN   Forces 1.5.7 State and explain the difference between scalars and vectors and give examples : None
Marie AAMANN   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Marie AAMANN   Light and waves 3.2.20 Describe how the reflection of sound may produce an echo : None
Marie AAMANN   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Marie AAMANN   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Marie AAMANN   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Marie AAMANN   Forces 1.6.1 a) Understand the concepts of momentum and impulse : None
Marie AAMANN   Forces 1.6.3 c) Recall and use the equation for impulse Ft = mv – mu : None
Marie AAMANN   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Nixon CHUNG   Motion and Measurement 1.2.9 Describe how acceleration and deceleration are related to changing speed.
Describe how this links to the gradient of a speed-time graph : None
Nixon CHUNG   Motion and Measurement 1.2.14 Describe in words the motion of bodies falling in a uniform gravitational field with air resistance (including reference to terminal velocity) : None
Nixon CHUNG   Forces 1.5.2 Recall and use the relation between (Resultant) force, mass and acceleration (including the direction)
 F = m x a : None
Nixon CHUNG   Light and waves 3.2.7 Recall and use the definition of refractive index n in terms of speed
 (Write the equation in words, and symbols with units. Draw the triangle) : None
Nixon CHUNG   Light and waves 3.2.4 Give the meaning of:
 · speed,
 · frequency
 · wavelength
 · amplitude : None
Nixon CHUNG   Light and waves 3.2.7 Recall and use the equation v = f λ : None
Nixon CHUNG   Light and waves 3.2.11 State that the speed of electromagnetic waves in a vaccum is 3.0x 108 m/s and is approximately the same in air.
 (You need to learn this number) : None
Nixon CHUNG   Light and waves 3.2.14 Describe the longitudinal nature of sound waves
 (Describe how a sound is transferred from a drum to your ear) : None
Nixon CHUNG   Light and waves 3.2.19 State the order of magnitude of the speed of sound in air, liquids and solids
 (You need to learn these approximate numbers) : None
Nixon CHUNG   Light and waves 3.2.22 Show an understanding of the term Ultrasound : None
Nixon CHUNG   Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
 : None
Nixon CHUNG   Pressure and density 1.8.1 a) Recall and use the equation p=F/A : None
Nixon CHUNG   Pressure and density 1.8.6 f) Recall and use the equation pressure=depth x gravity x density : None
Nixon CHUNG   Electricity 4.2.2.1 State that current is related to the flow of charge : None
Nixon CHUNG   Electricity 4.2.1.4 Show understanding that a current is a rate of flow of charge and recall and use the equation I = Q/t : None
for entry in entries:
    point = entry.syllabus_point
    sub_topic = point.sub_topic
    entry.syllabus_sub_topic=sub_topic
    entry.save()
Traceback (most recent call last):
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line 85, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line 303, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: UNIQUE constraint failed: journal_studentjournalentry.student_id, journal_studentjournalentry.syllabus_sub_topic_id
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "<input>", line 5, in <module>
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/base.py", line 729, in save
    force_update=force_update, update_fields=update_fields)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/base.py", line 759, in save_base
    updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/base.py", line 823, in _save_table
    forced_update)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/base.py", line 872, in _do_update
    return filtered._update(values) > 0
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 709, in _update
    return query.get_compiler(self.db).execute_sql(CURSOR)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 1375, in execute_sql
    cursor = super().execute_sql(result_type)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 1064, in execute_sql
    cursor.execute(sql, params)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line 85, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/utils.py", line 89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line 85, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line 303, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: UNIQUE constraint failed: journal_studentjournalentry.student_id, journal_studentjournalentry.syllabus_sub_topic_id
for point_entry in entries:
    point = point_entry.syllabus_point
    sub_topic = point.sub_topic
    sub_entry = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
    sub_entry.entry = sub_entry.entry.append(point_entry.entry)
Traceback (most recent call last):
  File "<input>", line 5, in <module>
AttributeError: 'tuple' object has no attribute 'entry'
for point_entry in entries:
    point = point_entry.syllabus_point
    sub_topic = point.sub_topic
    sub_entry = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
    sub_entry.entry = sub_entry.entry + point_entry.entry
Traceback (most recent call last):
  File "<input>", line 5, in <module>
AttributeError: 'tuple' object has no attribute 'entry'
entries[0]
<StudentJournalEntry: StudentJournalEntry object (388)>
point_entry = entries[0]
point = point_entry.syllabus_point
    sub_topic = point.sub_topic
  File "<input>", line 2
    sub_topic = point.sub_topic
    ^
IndentationError: unexpected indent
point = point_entry.syllabus_poinsub_topic = point.sub_topic
point = point_entry.syllabus_pointsub_topic = point.sub_topic
point = point_entry.syllabus_point
sub_topic = point.sub_topic
point
<SyllabusPoint: Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume>
sub_topic
<SyllabusSubTopic: Motion and Measurement: Measurement Techniques>
sub_entry = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
sub_entry.entry
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'entry'
sub_entry
(<StudentJournalEntry: StudentJournalEntry object (388)>, False)
for point_entry in entries:
    point = point_entry.syllabus_point
    sub_topic = point.sub_topic
    sub_entry, created = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
    sub_entry.entry = sub_entry.entry + point_entry.entry
Traceback (most recent call last):
  File "<input>", line 4, in <module>
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 487, in get_or_create
    return self.get(**lookup), False
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 407, in get
    (self.model._meta.object_name, num)
journal.models.MultipleObjectsReturned: get() returned more than one StudentJournalEntry -- it returned 171!
sub_entry = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 487, in get_or_create
    return self.get(**lookup), False
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 407, in get
    (self.model._meta.object_name, num)
journal.models.MultipleObjectsReturned: get() returned more than one StudentJournalEntry -- it returned 171!
sub_entry = StudentJournalEntry.filter(student=point_entry.student, syllabus_sub_topic=sub_topic)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: type object 'StudentJournalEntry' has no attribute 'filter'
sub_entry = StudentJournalEntry.objects.filter(student=point_entry.student, syllabus_sub_topic=sub_topic)
sub_entry
<QuerySet [<StudentJournalEntry: StudentJournalEntry object (462)>, <StudentJournalEntry: StudentJournalEntry object (463)>, <StudentJournalEntry: StudentJournalEntry object (464)>, <StudentJournalEntry: StudentJournalEntry object (465)>, <StudentJournalEntry: StudentJournalEntry object (467)>, <StudentJournalEntry: StudentJournalEntry object (469)>, <StudentJournalEntry: StudentJournalEntry object (470)>, <StudentJournalEntry: StudentJournalEntry object (471)>, <StudentJournalEntry: StudentJournalEntry object (472)>, <StudentJournalEntry: StudentJournalEntry object (473)>, <StudentJournalEntry: StudentJournalEntry object (474)>, <StudentJournalEntry: StudentJournalEntry object (475)>, <StudentJournalEntry: StudentJournalEntry object (476)>, <StudentJournalEntry: StudentJournalEntry object (477)>, <StudentJournalEntry: StudentJournalEntry object (478)>, <StudentJournalEntry: StudentJournalEntry object (479)>, <StudentJournalEntry: StudentJournalEntry object (480)>, <StudentJournalEntry: StudentJournalEntry object (481)>, <StudentJournalEntry: StudentJournalEntry object (482)>, <StudentJournalEntry: StudentJournalEntry object (483)>, '...(remaining elements truncated)...']>
point_entry.student
<Student: Marie AAMANN>
point_entry.syllabus_sub_topic
point_entry.sub_topic
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'StudentJournalEntry' object has no attribute 'sub_topic'
sub_topic
point
<SyllabusPoint: Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
>
point.sub_topic
orpahns = SyllabusPoint.objects.filter(sub_topic__isnull=True)
orphans
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'orphans' is not defined
orpahns
<QuerySet [<SyllabusPoint: Work energy and power 1.7.1 Demonstrate an understanding that an object may have energy due to its motion or its position, and that energy may be transferred and stored
>, <SyllabusPoint: Work energy and power 1.7.2 Give examples of energy in different forms, including kinetic, gravitational, chemical, strain, nuclear, internal, electrical, light and sound
>, <SyllabusPoint: Work energy and power 1.7.3 Give examples of the conversion of energy from one form to another, and of its transfer from one place to another
>, <SyllabusPoint: Work energy and power 1.7.4 Relate (without calculation) work done to the magnitude of a force and the distance moved
>, <SyllabusPoint: Work energy and power 1.7.5 Describe energy changes in terms of work done
>, <SyllabusPoint: Work energy and power 1.7.6 Recall and use:
 ΔW= F x d = ΔE
>, <SyllabusPoint: Work energy and power 1.7.7 Apply the principle of energy conservation to simple examples
>, <SyllabusPoint: Work energy and power 1.7.8 Relate (without calculation) power to work done and time taken, using appropriate examples
>, <SyllabusPoint: Work energy and power 1.7.9 Recall and use the equation P = E/t in simple systems
>, <SyllabusPoint: Work energy and power 1.7.11 Show a qualitative understanding of efficiency
>, <SyllabusPoint: Work energy and power 1.7.12 Recall and use the equation:
 efficiency = useful energy output/ Total energy input × 100%
>, <SyllabusPoint: Work energy and power 1.7.13 Distinguish between renewable and non-renewable sources of energy
>, <SyllabusPoint: Work energy and power 1.7.14 Describe how electricity or other useful forms of energy may be obtained from:
 – chemical energy stored in fuel
 – water, including the energy stored in waves, in tides, and in water behind hydroelectric dams
 – geothermal resources
 – nuclear fission
 – heat and light from the Sun (solar cells and panels)
>, <SyllabusPoint: Work energy and power 1.7.15 Give advantages and disadvantages of each method in terms of Economic, Reliability, Scale and Environmental impact
>, <SyllabusPoint: Work energy and power 1.7.16 Show an understanding that energy is released by nuclear fusion in the Sun
>]>
motion_topic = SyllabusTopic.object.get(pk=1)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: type object 'SyllabusTopic' has no attribute 'object'
motion_topic = SyllabusTopic.objects.get(pk=1)
wep_subtopic = SyllabusSubTopic.objects.get(pk=35)
wep_subtopic
<SyllabusSubTopic: Motion and Measurement: Work, energy and power>
for orphan in orpahns:
    orphan.topic = motion_topic
    orphan.sub_topic = wep_subtopic
    orphan.save()
for point_entry in entries:
    point = point_entry.syllabus_point
    sub_topic = point.sub_topic
    sub_entry, created = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
    sub_entry.entry = sub_entry.entry + point_entry.entry
Traceback (most recent call last):
  File "<input>", line 4, in <module>
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 487, in get_or_create
    return self.get(**lookup), False
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 407, in get
    (self.model._meta.object_name, num)
journal.models.MultipleObjectsReturned: get() returned more than one StudentJournalEntry -- it returned 171!
orpahns = SyllabusPoint.objects.filter(sub_topic__isnull=True)
orphans
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'orphans' is not defined
orpahns
<QuerySet []>
entries
<QuerySet [<StudentJournalEntry: StudentJournalEntry object (388)>, <StudentJournalEntry: StudentJournalEntry object (466)>, <StudentJournalEntry: StudentJournalEntry object (468)>, <StudentJournalEntry: StudentJournalEntry object (485)>, <StudentJournalEntry: StudentJournalEntry object (489)>, <StudentJournalEntry: StudentJournalEntry object (490)>, <StudentJournalEntry: StudentJournalEntry object (503)>, <StudentJournalEntry: StudentJournalEntry object (504)>, <StudentJournalEntry: StudentJournalEntry object (521)>, <StudentJournalEntry: StudentJournalEntry object (534)>, <StudentJournalEntry: StudentJournalEntry object (557)>, <StudentJournalEntry: StudentJournalEntry object (558)>, <StudentJournalEntry: StudentJournalEntry object (566)>, <StudentJournalEntry: StudentJournalEntry object (575)>, <StudentJournalEntry: StudentJournalEntry object (582)>, <StudentJournalEntry: StudentJournalEntry object (583)>, <StudentJournalEntry: StudentJournalEntry object (600)>, <StudentJournalEntry: StudentJournalEntry object (2205)>, <StudentJournalEntry: StudentJournalEntry object (2210)>, <StudentJournalEntry: StudentJournalEntry object (2221)>, '...(remaining elements truncated)...']>
point_entry = entries[0]
point = point_entry.syllabus_point
point
<SyllabusPoint: Motion and Measurement 1.1.1 Use and describe the use of rules and measuring cylinders to find a length or a volume>
point_entry.entry()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'str' object is not callable
print(point_entry.entry)
<p>correct value but incorrect unit&nbsp;<img alt="crying" height="23" src="https://www.greenpen.net/static/ckeditor/ckeditor/plugins/smiley/images/cry_smile.png" title="crying" width="23" /></p><p><strong>Entered from test [sample name] on 12/18/18</strong></p>Sample text
sub_topic = point.sub_topic
sub_entry, created = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
sub_entry
<StudentJournalEntry: StudentJournalEntry object (388)>
sub_entry.entry()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'str' object is not callable
sub_entry.entry
'<p>correct value but incorrect unit&nbsp;<img alt="crying" height="23" src="https://www.greenpen.net/static/ckeditor/ckeditor/plugins/smiley/images/cry_smile.png" title="crying" width="23" /></p><p><strong>Entered from test [sample name] on 12/18/18</strong></p>Sample text'
point_entry.entry
'<p>correct value but incorrect unit&nbsp;<img alt="crying" height="23" src="https://www.greenpen.net/static/ckeditor/ckeditor/plugins/smiley/images/cry_smile.png" title="crying" width="23" /></p><p><strong>Entered from test [sample name] on 12/18/18</strong></p>Sample text'
for point_entry in entries:
    point = point_entry.syllabus_point
    sub_topic = point.sub_topic
    sub_entry, created = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
    if sub_entry.entry == point_entry.entry:
        continue
    else:
        sub_entry.entry = sub_entry.entry + point_entry.entry
Traceback (most recent call last):
  File "<input>", line 4, in <module>
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 487, in get_or_create
    return self.get(**lookup), False
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 407, in get
    (self.model._meta.object_name, num)
journal.models.MultipleObjectsReturned: get() returned more than one StudentJournalEntry -- it returned 171!
point_entry
<StudentJournalEntry: StudentJournalEntry object (489)>
point_entry.student
<Student: Marie AAMANN>
point_entry.sub_topic
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'StudentJournalEntry' object has no attribute 'sub_topic'
point_entry.syllabus_sub_topic
point = point_entry.syllabus_point
point
<SyllabusPoint: Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
>
point.sub_topic
for point_entry in entries:
    point = point_entry.syllabus_point
    sub_topic = point.sub_topic
    sub_entry, created = StudentJournalEntry.objects.get_or_create(student=point_entry.student, syllabus_sub_topic=sub_topic)
    if sub_entry.entry == point_entry.entry:
        continue
    else:
        sub_entry.entry = sub_entry.entry + point_entry.entry
Traceback (most recent call last):
  File "<input>", line 4, in <module>
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 487, in get_or_create
    return self.get(**lookup), False
  File "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line 407, in get
    (self.model._meta.object_name, num)
journal.models.MultipleObjectsReturned: get() returned more than one StudentJournalEntry -- it returned 171!
entry
<StudentJournalEntry: StudentJournalEntry object (504)>
weirdos = StudentJournalEntry.filter(student=point_entry.student, syllabus_sub_topic=sub_topic)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: type object 'StudentJournalEntry' has no attribute 'filter'
weirdos = StudentJournalEntry.objects.filter(student=point_entry.student, syllabus_sub_topic=sub_topic)
weirdos
<QuerySet [<StudentJournalEntry: StudentJournalEntry object (462)>, <StudentJournalEntry: StudentJournalEntry object (463)>, <StudentJournalEntry: StudentJournalEntry object (464)>, <StudentJournalEntry: StudentJournalEntry object (465)>, <StudentJournalEntry: StudentJournalEntry object (467)>, <StudentJournalEntry: StudentJournalEntry object (469)>, <StudentJournalEntry: StudentJournalEntry object (470)>, <StudentJournalEntry: StudentJournalEntry object (471)>, <StudentJournalEntry: StudentJournalEntry object (472)>, <StudentJournalEntry: StudentJournalEntry object (473)>, <StudentJournalEntry: StudentJournalEntry object (474)>, <StudentJournalEntry: StudentJournalEntry object (475)>, <StudentJournalEntry: StudentJournalEntry object (476)>, <StudentJournalEntry: StudentJournalEntry object (477)>, <StudentJournalEntry: StudentJournalEntry object (478)>, <StudentJournalEntry: StudentJournalEntry object (479)>, <StudentJournalEntry: StudentJournalEntry object (480)>, <StudentJournalEntry: StudentJournalEntry object (481)>, <StudentJournalEntry: StudentJournalEntry object (482)>, <StudentJournalEntry: StudentJournalEntry object (483)>, '...(remaining elements truncated)...']>
point_entry.student
<Student: Marie AAMANN>
sub_topic
point
<SyllabusPoint: Work energy and power 1.7.10 Recall and use the expressions:
 KE = ½ mv 2 and
 GPE = mgh
>
point.sub_topic
point.pk
94
