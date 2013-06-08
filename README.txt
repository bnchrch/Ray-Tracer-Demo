README for CSC 305 assignment 4 authored by Ben Church v00732962

To compile and run:
	-open terminal
	-navigate to raytracer directory
	-type the following into the terminal: python raytrace.py [#of spheres] [recursion depth]
	- for example: "python raytrace.py 3 100" will create an image name raytrace.ppm with the dimensions 500x400 with a 3 spheres, a plane with a recursion depth of 100

	NOTE: to best demonstrate this file i would reccomend starting with
		-python raytrace.py 3 100
		-then 'python raytrace.py 2 100'
		-then 'python raytrace.py 1 100'
		-then finally 'python raytrace.py 3 1' to better see the phong illumination

Implemented criteria
	1/1 pt for code comments & README.txt file
	1/1 pt for writing an image to disk
	1/1 pt for generating the rays through each pixel and intersecting with a plane as floor
	1/1 pt for intersecting rays with a sphere
	1/1 pt for calculating the diffuse and specular color
	1/1 pt for calculating if a surface point is in the shadow or not
	1/1 pt for calculating reflections with arbitrary recursion depth
	0/1 pt for shooting an arbitrary number of rays per pixel
		-didnt know how to do that
	2/2 pt for combining Phong illumination with shadowing and reflections

What was done:
	I decided to use python as it was more expressive than C++ and I was more comfortable with it.

	raytrace.py:
		-initializes the Image class to create a byte array 500x400 and give the image file a name 'raytrace.ppm'
		-initializes the world with the recursion depth given by the user
		- then creates each Sphere object using the Sphere class with varying locations and random colors
		- each Sphere is also given an instance of the Material class which will be used to calculate colors
		-then the plane object is added to the world using the plane class and its own material
		-then I calculate my field of fiew: using a technique from: "http://stackoverflow.com/questions/13078243/ray-tracing-camera" and the tangent of my field of view degree which is 45 to find my width
			-width = 2tan(45 degrees in rads)
    		-height = (4/5) * tan(45 degress in rad) * 2.0
    		-pixelWidth = width / (499)
    		-pixelHeight = height / (399)

    	-then I create a ray for each pixel of the the screen converted to proper coordinates
    	-from each ray I use raycolor()to calculcate the final color
    	- then I save the color to it's position in the byte array it corresponds to
    	-After its all done I save the byte array to raytrace.ppm

    World.py:
    	init(rec):
    		-onbject array: contains each object and its material
    		-lightpoint: holds the light for the scene at (25,25,10)
    		-position: holds my camera position at (0,2,15)
    		-eyeDirection at (0,3,-1)
    		-bgColor which is white
    		-recDepth: the value I increment everytime I recursivley trace an array
    		-maxdepth: the maximum I will let recDepth get too

    	add(Object, Material):
    		-appends (object, material) to the object array for calling later

    	rayColor():
    		- essentially for every object I see if it intersects the ray then for everyobject that it does intersect I find the object that it the closes using firstIntersection()
    		-if no object is closest that means the ray hit nothing so i return the back ground color
    		-if an object is hit i call pixelColor() for the closest object using the ray, the position of the ray at time intersection and the normal
    		-In this function I also keep track of the recursionDepth and return the background color if the maxDepth is exceeded

    Material.py

    	init:
    		-Color: material color
    		-specular: specular coefficent
    		-difuse: difuse coef
    		-ambient: ambient coef

	    getPixelColor():
	    		-esentially I get the reflet vector and call rayColor() again to get the final pixel color and combine then multiply it by my specular coefficents and add it to my final color variable
	    		- then I create a ray from this point to the lightSource and see if it intersects an object to see if a shadow is cast
	    		-if no object blocks the curent objects light source:
	    			-I take the direction to the lightsource from the curent point and dot product it with the normal of the curerent point to get the diffuse power
	    			-i then multiply the diffusepower by my materials color and add it to the final color to create the lighting effect
	    		-finally I multiply my material color by my ambient coefficient and add it to the final color and return


	Image.py
		-all this is is an adaptation of the "to .ppm c++"" file given to us in the assignment

	reverseRay.py
		init:
			-point: holds the starting point
			-vector: holds the direction vector

		Position:
			- returns the location of the ray after time t

	Sphere.py
		-init:
			-centre: center point of the sphere
			-radius: radius of the sphere

		-intersection:
			-calculates the discriminant by
				-radius^2-((distance from centre to ray origin).(distance from centre to ray origin)-((distance from centre to ray origin).(ray trajectory))
			-if the discriminant is positive then there has been an intersection so i return the distance from the intersection to the ray starting point (t-sqrt(discriminant))
			-learned from the slides

		-getNormal
			-vector from arbitrary point to center normalized

	Plane.py
		--init:
			-point: center of the plane at 0,0,0
			-normal: normal facing up at 0,1,0

		-intersection:
			-if the ray is not perpendicular return 1/ray.normal

		-getNormal
			-returns the normal of the plane


	Vector()
		-not much explaining needed. containts the implementation of my vector and point classes to make calculations easier



